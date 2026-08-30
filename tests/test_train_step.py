import torch

from khuong.model import KhuongConfig, KhuongForCausalLM
from khuong.train import train_step


def test_train_step_updates_parameters():
    config = KhuongConfig(
        vocab_size=32,
        context_length=8,
        hidden_size=64,
        num_layers=2,
        num_attention_heads=4,
        num_kv_heads=2,
        ffn_hidden_size=128,
    )
    model = KhuongForCausalLM(config)
    optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3)
    batch = {"input_ids": torch.randint(0, 32, (2, 8)), "labels": torch.randint(0, 32, (2, 8))}
    before = model.embed_tokens.weight.detach().clone()
    loss = train_step(model, batch, optimizer)
    assert loss > 0
    assert not torch.equal(before, model.embed_tokens.weight.detach())
