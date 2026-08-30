import torch

from khuong.model import KhuongConfig, KhuongForCausalLM


def tiny_config() -> KhuongConfig:
    return KhuongConfig(vocab_size=97, context_length=16, hidden_size=32, num_layers=2, num_attention_heads=4, num_kv_heads=2, ffn_hidden_size=64)


def test_forward_shape_and_loss():
    model = KhuongForCausalLM(tiny_config())
    ids = torch.randint(0, 97, (2, 8))
    out = model(ids, ids)
    assert out["logits"].shape == (2, 8, 97)
    assert torch.isfinite(out["loss"])


def test_backward_produces_gradients():
    model = KhuongForCausalLM(tiny_config())
    ids = torch.randint(0, 97, (2, 8))
    loss = model(ids, ids)["loss"]
    loss.backward()
    assert model.embed_tokens.weight.grad is not None
    assert torch.isfinite(model.embed_tokens.weight.grad).all()


def test_tied_embedding_and_lm_head():
    model = KhuongForCausalLM(tiny_config())
    assert model.lm_head.weight.data_ptr() == model.embed_tokens.weight.data_ptr()
