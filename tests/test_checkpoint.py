import torch

from khuong.model import KhuongConfig, KhuongForCausalLM
from khuong.model.checkpoint import load_checkpoint, save_checkpoint


def test_checkpoint_round_trip(tmp_path):
    config = KhuongConfig(vocab_size=97, context_length=16, hidden_size=32, num_layers=2, num_attention_heads=4, num_kv_heads=2, ffn_hidden_size=48)
    model = KhuongForCausalLM(config)
    ids = torch.randint(0, config.vocab_size, (1, 6))
    before = model(ids)["logits"].detach()

    path = tmp_path / "khuong.pt"
    save_checkpoint(model, path)
    restored = load_checkpoint(path)
    after = restored(ids)["logits"].detach()

    assert restored.config == config
    assert torch.equal(before, after)


def test_checkpoint_rejects_unknown_format(tmp_path):
    path = tmp_path / "bad.pt"
    torch.save({"format_version": 999}, path)
    try:
        load_checkpoint(path)
    except ValueError as exc:
        assert "unsupported" in str(exc)
    else:
        raise AssertionError("invalid checkpoint was accepted")
