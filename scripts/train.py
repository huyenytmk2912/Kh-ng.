"""CLI entry point for a real Khuong training step."""

from __future__ import annotations

import argparse

import torch

from khuong.model import KhuongConfig, KhuongForCausalLM
from khuong.train import train_step


def main() -> None:
    parser = argparse.ArgumentParser(description="Train Khuong on a synthetic smoke batch.")
    parser.add_argument("--steps", type=int, default=1)
    parser.add_argument("--batch-size", type=int, default=1)
    parser.add_argument("--seq-len", type=int, default=32)
    parser.add_argument("--lr", type=float, default=1e-4)
    args = parser.parse_args()
    if args.steps < 1 or args.batch_size < 1 or args.seq_len < 2:
        raise SystemExit("steps/batch-size must be >= 1 and seq-len >= 2")

    # Small dimensions keep the CLI smoke test runnable on development machines.
    config = KhuongConfig(
        vocab_size=4096,
        context_length=max(128, args.seq_len),
        hidden_size=256,
        num_layers=4,
        num_attention_heads=8,
        num_kv_heads=2,
        ffn_hidden_size=512,
    )
    model = KhuongForCausalLM(config)
    optimizer = torch.optim.AdamW(model.parameters(), lr=args.lr)
    batch = {
        "input_ids": torch.randint(0, config.vocab_size, (args.batch_size, args.seq_len)),
        "labels": torch.randint(0, config.vocab_size, (args.batch_size, args.seq_len)),
    }
    for step in range(1, args.steps + 1):
        loss = train_step(model, batch, optimizer)
        print(f"step={step} loss={loss:.6f}")


if __name__ == "__main__":
    main()
