# Tư Duy Data Agent

## Mục tiêu
Tự động tìm tài liệu về tư duy, reasoning, problem solving, decision making và metacognition theo `tuduy.md`, sau đó chuyển hóa thành dữ liệu training tiếng Việt.

## Pipeline
1. Đọc `tuduy.md` để xác định taxonomy.
2. Tìm nguồn học thuật/open được phép sử dụng.
3. Xác minh nguồn và license/provenance.
4. Thu thập nội dung được phép.
5. Tóm lược kiến thức cốt lõi bằng tiếng Việt.
6. Chuyển thành tình huống, câu hỏi, bài toán và lời giải.
7. Tạo reasoning có cấu trúc, tránh suy luận giả.
8. Kiểm tra đáp án và loại mẫu trùng.
9. Gắn source, source_language và license_note.
10. Xuất JSONL vào `data/`.

## Schema
```json
{"id":"...","category":"...","language":"vi","source_language":"...","instruction":"...","input":"...","reasoning":"...","answer":"...","source":"...","license_note":"..."}
```

## Nhóm ưu tiên
- Suy luận logic
- Phân rã vấn đề
- Lập kế hoạch
- Ra quyết định
- Phát hiện lỗi trong lập luận
- So sánh phương án
- Metacognition
- Problem solving
- Reasoning dưới điều kiện không chắc chắn

## Quy tắc
- Không chỉ lấy tiêu đề hoặc metadata.
- Không sao chép nguyên văn nội dung có bản quyền không cho phép.
- Không bịa trích dẫn, nguồn hoặc license.
- Ưu tiên dữ liệu có thể kiểm chứng và bài tập có đáp án.
