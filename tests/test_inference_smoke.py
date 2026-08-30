import torch

from khuong.model import KhuongConfig, KhuongForCausalLM


def test_causal_lm_forward_and_greedy_shape():
    config = KhuongConfig(vocab_size=64, context_length=16, hidden_size=32, num_layers=1, num_attention_heads=4, num_kv_heads=2, ffn_hidden_size=64)
    model = KhuongForCausalLM(config).eval()
    input_ids = torch.randint(0, config.vocab_size, (1, 4))
    with torch.no_grad():
        outputs = model(input_ids)
    assert outputs["logits"].shape == (1, 4, config.vocab_size)
    next_token = outputs["logits"][:, -1, :].argmax(dim=-1)
    assert next_token.shape == (1,)
