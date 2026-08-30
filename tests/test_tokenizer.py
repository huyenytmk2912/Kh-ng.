from khuong.tokenizer import BasicTokenizer


def test_basic_tokenizer_round_trip():
    tokenizer = BasicTokenizer()
    text = "Khương đang học AI."
    ids = tokenizer.encode(text)
    assert ids[0] == tokenizer.bos_token_id
    assert ids[-1] == tokenizer.eos_token_id
    assert tokenizer.decode(ids) == text


def test_special_tokens_can_be_disabled():
    tokenizer = BasicTokenizer()
    ids = tokenizer.encode("xin chào", add_special_tokens=False)
    assert tokenizer.bos_token_id not in ids
    assert tokenizer.eos_token_id not in ids
