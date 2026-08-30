"""Batch collation for causal language modeling."""

from __future__ import annotations

import torch

from khuong.tokenizer import BaseTokenizer


def causal_collate(batch: list[dict[str, torch.Tensor]], tokenizer: BaseTokenizer) -> dict[str, torch.Tensor]:
    """Left-pad variable-length examples and mark padding labels as ignored."""
    if not batch:
        raise ValueError("batch must not be empty")
    max_len = max(item["input_ids"].numel() for item in batch)
    input_ids = torch.full((len(batch), max_len), tokenizer.pad_token_id, dtype=torch.long)
    labels = torch.full((len(batch), max_len), -100, dtype=torch.long)
    for row, item in enumerate(batch):
        ids = item["input_ids"]
        input_ids[row, : ids.numel()] = ids
        labels[row, : ids.numel()] = ids
    return {"input_ids": input_ids, "labels": labels}
