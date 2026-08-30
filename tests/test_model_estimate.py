from khuong.model import KhuongConfig, estimate_parameters


def test_target_model_estimate_is_finite_and_nontrivial():
    estimate = estimate_parameters(KhuongConfig())
    assert estimate.parameters > 100_000_000
    assert estimate.fp16_parameter_gib > 0
    assert estimate.bf16_parameter_gib == estimate.fp16_parameter_gib


def test_tiny_model_estimate_counts_tied_head_once():
    config = KhuongConfig(vocab_size=100, context_length=16, hidden_size=32, num_layers=1, num_attention_heads=4, num_kv_heads=2, ffn_hidden_size=64)
    estimate = estimate_parameters(config)
    assert estimate.parameters == 14080
