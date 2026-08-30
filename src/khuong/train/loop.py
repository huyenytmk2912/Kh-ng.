"""Minimal real training step for Khuong."""

from __future__ import annotations

import torch
from torch.optim import Optimizer

from ..model import KhuongForCausalLM


def train_step(
    model: KhuongForCausalLM,
    batch: dict[str, torch.Tensor],
    optimizer: Optimizer,
) -> float:
    """Run one forward/backward/update step and return scalar loss."""
    model.train()
    optimizer.zero_grad(set_to_none=True)
    outputs = model(batch["input_ids"], labels=batch["labels"])
    loss = outputs["loss"]
    loss.backward()
    optimizer.step()
    return float(loss.detach().cpu())
