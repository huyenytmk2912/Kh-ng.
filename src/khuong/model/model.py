"""Decoder-only Transformer model for Khuong."""

from __future__ import annotations

from dataclasses import dataclass

import torch
from torch import nn
import torch.nn.functional as F


@dataclass(frozen=True)
class KhuongConfig:
    """Architecture config: wide hidden state, deep stack, compact FFN."""

    vocab_size: int = 131072
    context_length: int = 2048
    hidden_size: int = 4096
    num_layers: int = 32
    num_attention_heads: int = 32
    num_kv_heads: int = 8
    ffn_hidden_size: int = 8192
    dropout: float = 0.0

    def __post_init__(self) -> None:
        positive = (
            self.vocab_size,
            self.context_length,
            self.hidden_size,
            self.num_layers,
            self.num_attention_heads,
            self.num_kv_heads,
            self.ffn_hidden_size,
        )
        if min(positive) <= 0:
            raise ValueError("model dimensions must be positive")
        if self.hidden_size % self.num_attention_heads:
            raise ValueError("hidden_size must be divisible by num_attention_heads")
        if self.num_attention_heads % self.num_kv_heads:
            raise ValueError("num_attention_heads must be divisible by num_kv_heads")
        if self.ffn_hidden_size < self.hidden_size:
            raise ValueError("ffn_hidden_size must be at least hidden_size")


class RMSNorm(nn.Module):
    def __init__(self, dim: int, eps: float = 1e-6) -> None:
        super().__init__()
        self.weight = nn.Parameter(torch.ones(dim))
        self.eps = eps

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return x * torch.rsqrt(x.pow(2).mean(-1, keepdim=True) + self.eps) * self.weight


def rotate_half(x: torch.Tensor) -> torch.Tensor:
    x1, x2 = x.chunk(2, dim=-1)
    return torch.cat((-x2, x1), dim=-1)


def apply_rope(q: torch.Tensor, k: torch.Tensor, positions: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
    dim = q.size(-1)
    inv_freq = 1.0 / (10000 ** (torch.arange(0, dim, 2, device=q.device, dtype=q.dtype) / dim))
    freqs = torch.einsum("s,d->sd", positions.to(q.dtype), inv_freq)
    emb = torch.cat((freqs, freqs), dim=-1)[None, None, :, :]
    cos, sin = emb.cos(), emb.sin()
    return q * cos + rotate_half(q) * sin, k * cos + rotate_half(k) * sin


class GQAAttention(nn.Module):
    def __init__(self, config: KhuongConfig) -> None:
        super().__init__()
        self.head_dim = config.hidden_size // config.num_attention_heads
        self.q_heads = config.num_attention_heads
        self.kv_heads = config.num_kv_heads
        self.repeat = self.q_heads // self.kv_heads
        self.q_proj = nn.Linear(config.hidden_size, self.q_heads * self.head_dim, bias=False)
        self.k_proj = nn.Linear(config.hidden_size, self.kv_heads * self.head_dim, bias=False)
        self.v_proj = nn.Linear(config.hidden_size, self.kv_heads * self.head_dim, bias=False)
        self.o_proj = nn.Linear(config.hidden_size, config.hidden_size, bias=False)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        b, s, _ = x.shape
        q = self.q_proj(x).view(b, s, self.q_heads, self.head_dim).transpose(1, 2)
        k = self.k_proj(x).view(b, s, self.kv_heads, self.head_dim).transpose(1, 2)
        v = self.v_proj(x).view(b, s, self.kv_heads, self.head_dim).transpose(1, 2)
        positions = torch.arange(s, device=x.device)
        q, k = apply_rope(q, k, positions)
        k = k.repeat_interleave(self.repeat, dim=1)
        v = v.repeat_interleave(self.repeat, dim=1)
        y = F.scaled_dot_product_attention(q, k, v, is_causal=True)
        return self.o_proj(y.transpose(1, 2).contiguous().view(b, s, -1))


class SwiGLU(nn.Module):
    def __init__(self, config: KhuongConfig) -> None:
        super().__init__()
        self.gate = nn.Linear(config.hidden_size, config.ffn_hidden_size, bias=False)
        self.up = nn.Linear(config.hidden_size, config.ffn_hidden_size, bias=False)
        self.down = nn.Linear(config.ffn_hidden_size, config.hidden_size, bias=False)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.down(F.silu(self.gate(x)) * self.up(x))


class TransformerBlock(nn.Module):
    def __init__(self, config: KhuongConfig) -> None:
        super().__init__()
        self.norm1 = RMSNorm(config.hidden_size)
        self.attn = GQAAttention(config)
        self.norm2 = RMSNorm(config.hidden_size)
        self.ffn = SwiGLU(config)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = x + self.attn(self.norm1(x))
        return x + self.ffn(self.norm2(x))


class KhuongForCausalLM(nn.Module):
    def __init__(self, config: KhuongConfig) -> None:
        super().__init__()
        self.config = config
        self.embed_tokens = nn.Embedding(config.vocab_size, config.hidden_size)
        self.layers = nn.ModuleList([TransformerBlock(config) for _ in range(config.num_layers)])
        self.norm = RMSNorm(config.hidden_size)
        self.lm_head = nn.Linear(config.hidden_size, config.vocab_size, bias=False)
        self.lm_head.weight = self.embed_tokens.weight

    def forward(self, input_ids: torch.Tensor, labels: torch.Tensor | None = None) -> dict[str, torch.Tensor]:
        if input_ids.ndim != 2:
            raise ValueError("input_ids must have shape [batch, sequence]")
        if input_ids.size(1) > self.config.context_length:
            raise ValueError("sequence exceeds context_length")
        x = self.embed_tokens(input_ids)
        for layer in self.layers:
            x = layer(x)
        logits = self.lm_head(self.norm(x))
        out = {"logits": logits}
        if labels is not None:
            if labels.shape != input_ids.shape:
                raise ValueError("labels must match input_ids shape")
            out["loss"] = F.cross_entropy(
                logits[:, :-1].reshape(-1, logits.size(-1)),
                labels[:, 1:].reshape(-1),
            )
        return out
