"""Minimal runtime boundary for the Khuong platform layer."""

from __future__ import annotations

from dataclasses import dataclass

from .contracts import ModelMetadata, TokenSequence, validate_compatibility


@dataclass(frozen=True)
class RuntimeConfig:
    context_length: int
    tokenizer_version: str


class RuntimeSession:
    """Validates model/tokenizer inputs before inference is implemented."""

    def __init__(self, model: ModelMetadata, config: RuntimeConfig) -> None:
        model.validate()
        if config.context_length <= 0:
            raise ValueError("context_length must be positive")
        self.model = model
        self.config = config

    def validate_input(self, tokens: TokenSequence) -> None:
        validate_compatibility(
            self.model,
            tokens,
            context_length=self.config.context_length,
            tokenizer_version=self.config.tokenizer_version,
        )

    def prepare(self, tokens: TokenSequence) -> tuple[int, ...]:
        self.validate_input(tokens)
        return tokens.ids
