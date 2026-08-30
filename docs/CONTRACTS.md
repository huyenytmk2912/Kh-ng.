# Khương — Contracts v0

> Giai đoạn 1.3/1.4. Đây là contract nền tảng, chưa tuyên bố implementation production.

## 1. Nguyên tắc

- Contract là giao diện ổn định giữa các lớp.
- Payload phải có version để hỗ trợ compatibility.
- Không truyền implementation detail qua boundary.
- Input/output phải validate trước khi chuyển lớp.
- Breaking change phải tăng contract version và cập nhật test.

## 2. Text ↔ Tokenizer contract

### Encode

```text
encode(text: UTF-8 string) -> TokenSequence
```

`TokenSequence` gồm:
- `ids: list[int]`
- `tokenizer_version: string`
- `vocab_size: int`
- `special_token_ids: map[string, int]`

Invariant:
- mọi ID thuộc `[0, vocab_size)`;
- text là UTF-8;
- metadata phải khớp artifact tokenizer.

### Decode

```text
decode(ids: list[int]) -> UTF-8 string
```

Input IDs ngoài vocab phải bị từ chối.

## 3. Tokenizer ↔ Model contract

Model nhận `input_ids` dạng integer tensor với shape:

```text
[batch, sequence_length]
```

Invariant:
- dtype integer phù hợp backend;
- `0 <= input_id < vocab_size`;
- `sequence_length <= context_length`;
- `vocab_size` và special IDs phải khớp model metadata.

## 4. Model contract

### Input

```text
input_ids: [B, T]
attention/context state: optional
KV cache: optional
```

### Output

```text
logits: [B, T, V]
KV cache: optional
```

Trong đó `V = vocab_size`.

Model phải expose metadata tối thiểu:

```text
architecture
vocab_size
context_length
num_layers
hidden_size
num_attention_heads
num_kv_heads
ffn_hidden_size
position_encoding
normalization
activation
tied_embeddings
model_version
```

## 5. Runtime contract

```text
load(artifact) -> RuntimeSession
prefill(input_ids) -> RuntimeState
decode(state, sampling_config) -> TokenStep
stream(state) -> TokenStream
```

Runtime chịu trách nhiệm:
- validate manifest;
- kiểm tra compatibility model/tokenizer;
- chọn device/backend;
- quản lý KV cache;
- stop conditions;
- resource/error handling.

Runtime không được chứa logic mission/planning/agent.

## 6. Artifact contract

Artifact bundle tối thiểu:

```text
manifest.json
config.json
model weights
 tokenizer artifact
runtime config
metadata
checksums
```

`manifest.json` phải khai báo version, model architecture, tokenizer version, vocab size, context length và checksum của thành phần quan trọng.

## 7. Compatibility rules

Runtime phải từ chối artifact nếu:

- checksum không hợp lệ;
- manifest thiếu trường bắt buộc;
- tokenizer/model vocab không khớp;
- special token IDs không khớp;
- context length không được runtime hỗ trợ;
- artifact version không tương thích.

## 8. Verification requirement

Mỗi contract quan trọng phải có:

1. schema/shape validation;
2. positive test;
3. negative test;
4. integration test giữa hai boundary;
5. reproducible evidence.

## 9. Status

- Architecture: 🟡 Đang khóa contract nền tảng.
- Model ↔ Tokenizer: 🟡 Contract v0.
- Runtime ↔ Artifact: 🟡 Contract v0.
- Production implementation: ⬜ Chưa làm.
