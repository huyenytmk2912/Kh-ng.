"""Tokenizer contract used by Khuong training and inference."""

from __future__ import annotations

from abc import ABC, abstractmethod


class BaseTokenizer(ABC):
    """Stable tokenizer API; concrete vocabulary implementation comes later."""

    pad_token_id: int
    bos_token_id: int
    eos_token_id: int

    @abstractmethod
    def encode(self, text: str, *, add_special_tokens: bool = True) -> list[int]:
        raise NotImplementedError

    @abstractmethod
    def decode(self, token_ids: list[int]) -> str:
        raise NotImplementedError

    def batch_encode(self, texts: list[str], *, add_special_tokens: bool = True) -> list[list[int]]:
        return [self.encode(text, add_special_tokens=add_special_tokens) for text in texts]
