"""Safe checkpoint serialization for Khuong models."""

from __future__ import annotations

from pathlib import Path
import json

import torch

from .model import KhuongConfig, KhuongForCausalLM

FORMAT_VERSION = 1


def save_checkpoint(model: KhuongForCausalLM, path: str | Path) -> None:
    """Save model weights and architecture metadata in a versioned checkpoint."""
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "format_version": FORMAT_VERSION,
        "config": model.config.__dict__,
        "state_dict": model.state_dict(),
    }
    torch.save(payload, target)


def load_checkpoint(path: str | Path, *, map_location: str | torch.device = "cpu") -> KhuongForCausalLM:
    """Load a checkpoint and validate its format before constructing the model."""
    payload = torch.load(Path(path), map_location=map_location, weights_only=False)
    if not isinstance(payload, dict) or payload.get("format_version") != FORMAT_VERSION:
        raise ValueError("unsupported or invalid Khuong checkpoint")
    config_data = payload.get("config")
    state_dict = payload.get("state_dict")
    if not isinstance(config_data, dict) or not isinstance(state_dict, dict):
        raise ValueError("checkpoint is missing config or state_dict")
    model = KhuongForCausalLM(KhuongConfig(**config_data))
    model.load_state_dict(state_dict, strict=True)
    return model
