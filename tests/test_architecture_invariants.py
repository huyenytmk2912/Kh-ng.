from khuong.model import KhuongConfig


def test_64_layer_architecture_invariants():
    config = KhuongConfig()
    assert config.num_layers == 64
    assert config.hidden_size == 4096
    assert config.ffn_hidden_size == 8192
    assert config.num_attention_heads == 32
    assert config.num_kv_heads == 8
