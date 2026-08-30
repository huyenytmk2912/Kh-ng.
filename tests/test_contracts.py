from khuong.contracts import ArtifactManifest, ModelMetadata, TokenSequence, validate_compatibility


def model():
    return ModelMetadata(
        model_version="1.0.0",
        architecture="decoder-only-transformer",
        vocab_size=131072,
        context_length=4096,
        num_layers=24,
        hidden_size=2048,
        num_attention_heads=16,
        num_kv_heads=8,
        ffn_hidden_size=3072,
        position_encoding="RoPE",
        normalization="RMSNorm",
        activation="SwiGLU",
        tied_embeddings=True,
    )


def test_valid_token_model_compatibility():
    tokens = TokenSequence((1, 2, 131071), "tok-1", 131072, {"bos": 1})
    validate_compatibility(model(), tokens, context_length=4096, tokenizer_version="tok-1")


def test_rejects_out_of_range_token():
    tokens = TokenSequence((131072,), "tok-1", 131072)
    try:
        tokens.validate()
    except ValueError:
        return
    raise AssertionError("expected out-of-range token to fail")


def test_rejects_vocab_mismatch():
    tokens = TokenSequence((1,), "tok-1", 100000)
    try:
        validate_compatibility(model(), tokens, context_length=1, tokenizer_version="tok-1")
    except ValueError:
        return
    raise AssertionError("expected vocab mismatch to fail")


def test_rejects_context_overflow():
    tokens = TokenSequence((1,) * 4097, "tok-1", 131072)
    try:
        validate_compatibility(model(), tokens, context_length=4097, tokenizer_version="tok-1")
    except ValueError:
        return
    raise AssertionError("expected context overflow to fail")


def test_manifest_requires_checksums():
    manifest = ArtifactManifest("1", model(), "tok-1", {})
    try:
        manifest.validate()
    except ValueError:
        return
    raise AssertionError("expected missing checksums to fail")
