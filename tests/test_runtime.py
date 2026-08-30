from khuong.contracts import ModelMetadata, TokenSequence
from khuong.runtime import RuntimeConfig, RuntimeSession


def model():
    return ModelMetadata("1.0.0", "decoder-only-transformer", 131072, 4096, 24, 2048, 16, 8, 3072, "RoPE", "RMSNorm", "SwiGLU", True)


def test_runtime_prepares_valid_input():
    runtime = RuntimeSession(model(), RuntimeConfig(4096, "tok-1"))
    tokens = TokenSequence((1, 42, 131071), "tok-1", 131072)
    assert runtime.prepare(tokens) == (1, 42, 131071)


def test_runtime_rejects_wrong_tokenizer_version():
    runtime = RuntimeSession(model(), RuntimeConfig(4096, "tok-1"))
    tokens = TokenSequence((1,), "tok-2", 131072)
    try:
        runtime.prepare(tokens)
    except ValueError as exc:
        assert "version" in str(exc)
    else:
        raise AssertionError("runtime accepted incompatible tokenizer")
