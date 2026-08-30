"""CLI entry point for resumable Khuong training smoke runs."""

from __future__ import annotations

import argparse

import torch

from khuong.model import KhuongConfig, KhuongForCausalLM
from khuong.train import load_checkpoint, save_checkpoint, train_step


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a resumable Khuong training smoke run.")
    parser.add_argument("--steps", type=int, default=1)
    parser.add_argument("--batch-size", type=int, default=1)
    parser.add_argument("--seq-len", type=int, default=32)
    parser.add_argument("--lr", type=float, default=1e-4)
    parser.add_argument("--checkpoint", default="checkpoints/latest.pt")
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--save-every", type=int, default=1)
    args = parser.parse_args()
    if args.steps < 1 or args.batch_size < 1 or args.seq_len < 2 or args.save_every < 1:
        raise SystemExit("steps/batch-size/save-every must be >= 1 and seq-len >= 2")

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
    start_step = 0
    if args.resume:
        try:
            start_step = load_checkpoint(args.checkpoint, model, optimizer)
        except FileNotFoundError as exc:
            raise SystemExit(f"checkpoint not found: {args.checkpoint}") from exc

    batch = {
        "input_ids": torch.randint(0, config.vocab_size, (args.batch_size, args.seq_len)),
        "labels": torch.randint(0, config.vocab_size, (args.batch_size, args.seq_len)),
    }
    for step in range(start_step + 1, start_step + args.steps + 1):
        loss = train_step(model, batch, optimizer)
        print(f"step={step} loss={loss:.6f}")
        if step % args.save_every == 0:
            save_checkpoint(args.checkpoint, model, optimizer, step)
            print(f"checkpoint={args.checkpoint}")


if __name__ == "__main__":
    main()
