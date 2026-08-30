import torch

from khuong.data.collator import causal_collate
from khuong.data.text import CausalTextDataset
from khuong.tokenizer import BasicTokenizer


def test_causal_dataset_and_collator():
    tokenizer = BasicTokenizer()
    dataset = CausalTextDataset(["xin chào", "Khương học AI"], tokenizer, sequence_length=8)
    assert len(dataset) > 0
    batch = causal_collate([dataset[0]], tokenizer)
    assert batch["input_ids"].shape == batch["labels"].shape
    assert batch["input_ids"].dtype == torch.long
