# Khương — Quy ước phát triển

## Trạng thái

- ⬜ Chưa làm
- 🟡 Đang làm
- 🟢 Đã xong
- 🔴 Có lỗi cần mở lại
- ⚪ Bị chặn

## Definition of Done

Một hạng mục chỉ được coi là hoàn thành khi có:

1. Implementation thực tế.
2. Unit/integration test phù hợp.
3. Verification tối thiểu hai lượt theo nhiệm vụ.
4. Evidence có thể kiểm tra lại.
5. Không có regression đã biết.

## Quy tắc repository

- `src/` chứa production code.
- `tests/` chứa test.
- `docs/` chứa tài liệu kỹ thuật và kiến trúc.
- `configs/` chứa cấu hình không chứa secret.
- `scripts/` chứa tiện ích build/test/dev.
- `artifacts/` chỉ dành cho metadata/manifest nhỏ; weights lớn không commit trực tiếp.
- Secret và credential không được đưa vào repository.

## Quy tắc commit

Commit phải nhỏ, có mục đích rõ ràng và mô tả đúng thay đổi. Không trộn refactor lớn với feature không liên quan.

## Quy tắc evidence

Mỗi thành phần quan trọng cần ghi lại command, test result, benchmark hoặc artifact verification đủ để người khác tái hiện kết luận.
