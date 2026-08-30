from khuong.model import KhuongConfig, estimate_parameters


def test_target_architecture_depth_and_size():
    config = KhuongConfig()
    estimate = estimate_parameters(config)
    assert config.hidden_size == 4096
    assert config.num_layers == 64
    assert config.ffn_hidden_size == 8192
    assert estimate.parameters > 2_000_000_000
