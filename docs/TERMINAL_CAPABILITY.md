# Khương — Terminal Capability

## Mục tiêu

Khương phải có khả năng yêu cầu thực thi terminal trực tiếp từ model/runtime mà không bắt buộc phải có Agent orchestration.

## Boundary

```text
Model
  ↓ tool/action request
TerminalCapability
  ↓ policy
OS process
  ↓
stdout / stderr / exit code
  ↓
Model
```

Agent vẫn có thể dùng capability này, nhưng Agent không phải dependency bắt buộc.

## Security boundary

`TerminalCapability` không chạy shell tự do. Command phải đi qua allowlist/denylist, working directory bị giới hạn trong terminal root và timeout có giới hạn.

Kết quả thực thi luôn gồm command, cwd, stdout, stderr, exit code và trạng thái timeout để tầng reasoning/verification có evidence.

Không truyền credential hoặc secret vào environment của process trừ khi policy/runtime đã thiết kế và kiểm soát rõ ràng.

## Hiện thực

- `src/khuong/terminal.py` — capability và policy.
- `tests/test_terminal.py` — execution, policy, root confinement và timeout.

## Chế độ sử dụng

### Direct tool mode

`Model → TerminalCapability → Model`

Dùng cho thao tác ngắn và có policy rõ.

### Agent mode

`Model → Planner/Agent → TerminalCapability → Verification`

Dùng cho mission nhiều bước.

## Nguyên tắc

1. Terminal là capability/runtime service, không phải một phần của model weights.
2. Agent là orchestration layer tùy chọn.
3. Mọi command model yêu cầu phải chịu policy enforcement.
4. Không đánh dấu production-ready khi chưa có integration test và security review đầy đủ.
