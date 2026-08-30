"""Checkpoint save/load helpers for resumable training."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import torch
from torch.optim import Optimizer

from ..model import KhuongForCausalLM


def save_checkpoint(
    path: str | Path,
    model: KhuongForCausalLM,
    optimizer: Optimizer,
    step: int,
) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    torch.save(
        {
            "step": step,
            "model": model.state_dict(),
            "optimizer": optimizer.state_dict(),
            "config": model.config.__dict__,
        },
        path,
    )


def load_checkpoint(
    path: str | Path,
    model: KhuongForCausalLM,
    optimizer: Optimizer,
    *,
    map_location: str | torch.device = "cpu",
) -> int:
    checkpoint: dict[str, Any] = torch.load(path, map_location=map_location, weights_only=False)
    model.load_state_dict(checkpoint["model"])
    optimizer.load_state_dict(checkpoint["optimizer"])
    return int(checkpoint["step"])
