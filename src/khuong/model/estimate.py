"""Parameter and memory estimates for Khuong model configurations."""

from __future__ import annotations

from dataclasses import dataclass

from .model import KhuongConfig


@dataclass(frozen=True)
class ModelEstimate:
    parameters: int
    parameter_memory_bytes: int
    fp16_parameter_gib: float
    bf16_parameter_gib: float


def estimate_parameters(config: KhuongConfig) -> ModelEstimate:
    d = config.hidden_size
    h = config.num_attention_heads
    kv = config.num_kv_heads
    f = config.ffn_hidden_size
    vocab = config.vocab_size
    layers = config.num_layers
    head_dim = d // h

    embedding = vocab * d
    attention = d * (h * head_dim + 2 * kv * head_dim + d)
    ffn = 3 * d * f
    norms = 2 * d
    final_norm = d
    total = embedding + layers * (attention + ffn + norms) + final_norm

    # lm_head is tied to embeddings, so it is not counted twice.
    return ModelEstimate(
        parameters=total,
        parameter_memory_bytes=total * 4,
        fp16_parameter_gib=total * 2 / 1024**3,
        bf16_parameter_gib=total * 2 / 1024**3,
    )
