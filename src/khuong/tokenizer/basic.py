"""Deterministic baseline tokenizer for development and pipeline tests.

This is intentionally not the production vocabulary. A trained tokenizer can
implement BaseTokenizer later without changing model/training interfaces.
"""

from __future__ import annotations

import re

from .base import BaseTokenizer


class BasicTokenizer(BaseTokenizer):
    pad_token_id = 0
    bos_token_id = 1
    eos_token_id = 2
    unk_token_id = 3

    def __init__(self) -> None:
        self._token_to_id = {"<pad>": 0, "<bos>": 1, "<eos>": 2, "<unk>": 3}
        self._id_to_token = {v: k for k, v in self._token_to_id.items()}

    def encode(self, text: str, *, add_special_tokens: bool = True) -> list[int]:
        pieces = re.findall(r"\w+|[^\w\s]", text, flags=re.UNICODE)
        ids: list[int] = []
        if add_special_tokens:
            ids.append(self.bos_token_id)
        for piece in pieces:
            token_id = self._token_to_id.setdefault(piece, len(self._token_to_id))
            self._id_to_token[token_id] = piece
            ids.append(token_id)
        if add_special_tokens:
            ids.append(self.eos_token_id)
        return ids

    def decode(self, token_ids: list[int]) -> str:
        pieces = []
        for token_id in token_ids:
            if token_id in (self.pad_token_id, self.bos_token_id, self.eos_token_id):
                continue
            pieces.append(self._id_to_token.get(token_id, "<unk>"))
        text = " ".join(pieces)
        return re.sub(r"\s+([,.;:!?%])", r"\1", text)
