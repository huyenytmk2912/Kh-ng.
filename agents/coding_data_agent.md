# Coding Data Agent

## Mục tiêu
Tự động tìm tài liệu coding được phép sử dụng, thu thập nội dung thực tế, chuẩn hóa và chuyển hóa thành dữ liệu training tiếng Việt cho Khương.

## Pipeline
1. Đọc `coding.md` để xác định taxonomy và mục tiêu.
2. Discover nguồn phù hợp.
3. Verify license/provenance.
4. Thu thập nội dung được phép.
5. Loại trùng và làm sạch.
6. Chuyển hóa sang tiếng Việt.
7. Tạo instruction, input, reasoning, answer.
8. Kiểm tra tính đúng đắn bằng test/example khi có thể.
9. Ghi source, source_language, license_note.
10. Xuất JSONL vào `data/`.

## Schema
```json
{"id":"...","category":"...","language":"vi","source_language":"...","instruction":"...","input":"...","reasoning":"...","answer":"...","category_source":"...","license_note":"..."}
```

## Quy tắc chất lượng
- Không chỉ lưu tiêu đề; phải có nội dung training thực tế.
- Ưu tiên nguồn mở, có license rõ ràng.
- Không sao chép nguyên văn tài liệu có bản quyền không cho phép.
- Không bịa source hoặc license.
- Ưu tiên dữ liệu đa dạng: thuật toán, cấu trúc dữ liệu, debugging, testing, SWE, web, Python, C++, JavaScript.
