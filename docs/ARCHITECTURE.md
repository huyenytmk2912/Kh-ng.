# Khương — Kiến trúc hệ thống

> Tài liệu kiến trúc canonical. Đây là thiết kế mục tiêu; chỉ đánh dấu thành phần đã triển khai khi có code, test và evidence.

## 1. Mục tiêu

Khương hướng tới một AI local-first có khả năng nhận mission nhiều bước, lập kế hoạch, thực hiện hành động, quan sát, kiểm chứng, phục hồi và duy trì trạng thái.

Luồng tổng quát:

```text
Goal
  ↓
Mission / Planner
  ↓
Agent Executor
  ↓
Tools / Skills
  ↓
Observation
  ↓
Verification
  ↓
State / Memory Update
  ↓
Next Action / Complete / Recover
```

## 2. Các lớp canonical

```text
Interface
  API / UI
       ↓
Orchestration
  Mission / Agent / Planner / Executor
       ↓
Cognition
  Reasoning / Verification / Recovery
       ↓
State
  Context / State / Memory / Knowledge
       ↓
Capabilities
  Tools / Skills / Capability Registry
       ↓
Inference
  Runtime / Model / Tokenizer
       ↓
Infrastructure
  Device / Storage / Logging / Evaluation
```

## 3. Dependency direction

Các lớp phía trên được phép phụ thuộc abstraction của lớp phía dưới; lớp thấp hơn không được phụ thuộc ngược vào orchestration hoặc UI.

- UI/API → Mission/Agent
- Mission/Agent → Reasoning/Planning/Tools/Memory/Verification
- Reasoning/Planning → Model/Runtime + State/Context
- Memory/Knowledge → Storage abstraction
- Tools → capability contracts
- Runtime → Model + Tokenizer + device backend
- Evaluation → public contracts, không điều khiển production logic

## 4. Boundary contracts

### Model
Nhận token IDs và model state; trả logits/hidden outputs theo contract đã định nghĩa.

### Tokenizer
Text ↔ token IDs; quản lý special tokens, vocab metadata và compatibility.

### Runtime
Chịu trách nhiệm loading artifact, device selection, prefill/decode, KV cache, sampling, streaming và resource/error handling.

### State / Context
Quản lý trạng thái hiện tại của user, project, mission, task, environment và tools; kiểm soát context budget và compaction.

### Memory
Working, episodic, semantic và project memory; lưu/truy xuất/rank thông tin kèm provenance.

### Agent
Điều phối mission, planner, executor, observer, verifier và recovery.

### Tools / Skills
Capability có contract, validation, permissions, input/output schema và observable result.

### Verification
Đánh giá output/action dựa trên expected result, evidence hoặc tool; trả trạng thái pass/fail/uncertain và thông tin chẩn đoán.

### Evaluation
Golden tasks, metrics, traces, replay, regression gates và before/after comparison.

## 5. Artifact contract

Một model artifact production phải có tối thiểu:

```text
weights
config
 tokenizer
runtime config
metadata
version
checksum
manifest
```

Artifact phải được validate trước khi runtime sử dụng.

## 6. Quy tắc thay đổi kiến trúc

1. Không tạo implementation trùng canonical architecture.
2. Không đánh dấu hoàn thành nếu thiếu evidence.
3. Thay đổi boundary phải cập nhật tài liệu và test liên quan.
4. Regression phải mở lại trạng thái thành phần bị ảnh hưởng.
5. Ưu tiên interface ổn định và backend có thể thay thế.
