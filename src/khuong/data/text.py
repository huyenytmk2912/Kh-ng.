"""Tokenized causal-language-model dataset utilities."""

from __future__ import annotations

import torch
from torch.utils.data import Dataset

from khuong.tokenizer import BaseTokenizer


class CausalTextDataset(Dataset[dict[str, torch.Tensor]]):
    """Convert text samples into fixed-length next-token-training examples."""

    def __init__(self, texts: list[str], tokenizer: BaseTokenizer, sequence_length: int) -> None:
        if sequence_length < 2:
            raise ValueError("sequence_length must be at least 2")
        self.examples: list[list[int]] = []
        for text in texts:
            ids = tokenizer.encode(text)
            if len(ids) < 2:
                continue
            for start in range(0, len(ids) - 1, sequence_length):
                chunk = ids[start : start + sequence_length]
                if len(chunk) >= 2:
                    self.examples.append(chunk)

    def __len__(self) -> int:
        return len(self.examples)

    def __getitem__(self, index: int) -> dict[str, torch.Tensor]:
        ids = torch.tensor(self.examples[index], dtype=torch.long)
        return {"input_ids": ids, "labels": ids.clone()}
