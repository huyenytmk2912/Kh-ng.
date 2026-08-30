"""Versioned contracts shared by tokenizer, model, and runtime."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Mapping, Sequence

CONTRACT_VERSION = "0.1"


@dataclass(frozen=True)
class TokenSequence:
    ids: tuple[int, ...]
    tokenizer_version: str
    vocab_size: int
    special_token_ids: Mapping[str, int] = field(default_factory=dict)

    def validate(self) -> None:
        if self.vocab_size <= 0:
            raise ValueError("vocab_size must be positive")
        if any(not isinstance(token_id, int) for token_id in self.ids):
            raise TypeError("token IDs must be integers")
        if any(token_id < 0 or token_id >= self.vocab_size for token_id in self.ids):
            raise ValueError("token ID is outside vocabulary range")
        for name, token_id in self.special_token_ids.items():
            if not isinstance(name, str) or not isinstance(token_id, int):
                raise TypeError("special token metadata is invalid")
            if token_id < 0 or token_id >= self.vocab_size:
                raise ValueError("special token ID is outside vocabulary range")


@dataclass(frozen=True)
class ModelMetadata:
    model_version: str
    architecture: str
    vocab_size: int
    context_length: int
    num_layers: int
    hidden_size: int
    num_attention_heads: int
    num_kv_heads: int
    ffn_hidden_size: int
    position_encoding: str
    normalization: str
    activation: str
    tied_embeddings: bool

    def validate(self) -> None:
        positive = {
            "vocab_size": self.vocab_size,
            "context_length": self.context_length,
            "num_layers": self.num_layers,
            "hidden_size": self.hidden_size,
            "num_attention_heads": self.num_attention_heads,
            "num_kv_heads": self.num_kv_heads,
            "ffn_hidden_size": self.ffn_hidden_size,
        }
        if any(value <= 0 for value in positive.values()):
            raise ValueError("model dimensions must be positive")
        if self.num_attention_heads % self.num_kv_heads != 0:
            raise ValueError("attention heads must be divisible by KV heads")


@dataclass(frozen=True)
class ArtifactManifest:
    artifact_version: str
    model: ModelMetadata
    tokenizer_version: str
    checksums: Mapping[str, str]
    contract_version: str = CONTRACT_VERSION

    def validate(self) -> None:
        if not self.artifact_version or not self.tokenizer_version:
            raise ValueError("artifact and tokenizer versions are required")
        if self.contract_version != CONTRACT_VERSION:
            raise ValueError("unsupported contract version")
        self.model.validate()
        if not self.checksums:
            raise ValueError("artifact checksums are required")
        if any(not name or not digest for name, digest in self.checksums.items()):
            raise ValueError("invalid artifact checksum metadata")


def validate_compatibility(
    model: ModelMetadata,
    tokens: TokenSequence,
    *,
    context_length: int,
    tokenizer_version: str,
) -> None:
    """Validate the tokenizer/model boundary before inference."""
    model.validate()
    tokens.validate()
    if tokens.vocab_size != model.vocab_size:
        raise ValueError("model/tokenizer vocab size mismatch")
    if tokens.tokenizer_version != tokenizer_version:
        raise ValueError("tokenizer version mismatch")
    if len(tokens.ids) > model.context_length:
        raise ValueError("sequence exceeds model context length")
    if context_length > model.context_length:
        raise ValueError("requested context exceeds model context length")
