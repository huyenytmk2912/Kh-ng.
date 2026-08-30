# Coding Training Corpus

Mục tiêu: xây dựng kho 10.000 tài liệu/bài tập coding có thể dùng hợp pháp cho việc học và chuẩn bị dữ liệu training AI.

## Nhóm nội dung

### 1. Problem solving
- Thuật toán và cấu trúc dữ liệu
- Competitive programming
- Bài tập theo mức độ dễ → khó
- Problem statement + test cases + solution khi license cho phép

### 2. Ngôn ngữ lập trình
- Python
- JavaScript / TypeScript
- C / C++
- Java
- Go
- Rust
- C#
- Kotlin
- Swift
- PHP
- Ruby

### 3. Web development
- HTML/CSS
- JavaScript
- React
- Node.js
- Backend/API
- Database/SQL
- Authentication
- Testing
- Deployment

### 4. Software engineering
- Git/GitHub
- Clean code
- Design patterns
- Debugging
- Unit/integration testing
- CI/CD
- System design

### 5. AI/ML coding
- NumPy/PyTorch
- Data processing
- Model training
- Fine-tuning
- Evaluation
- Inference
- Computer vision
- NLP
- LLM tooling

## Nguồn ưu tiên

1. Project CodeNet — tập dữ liệu lớn về bài toán lập trình và submissions; kiểm tra license trước khi tái phân phối.
2. AtCoder datasets — problem statements và accepted solutions có điều khoản sử dụng riêng cho AI training; tuân thủ license/terms.
3. Exercism — bài tập thực hành nhiều ngôn ngữ; kiểm tra license từng phần trước khi đưa vào corpus.
4. The Odin Project — curriculum và project học web mã nguồn mở; ưu tiên liên kết tới nguồn thay vì sao chép nội dung có bản quyền.
5. Microsoft Python Programming Puzzles — bài toán Python phục vụ nghiên cứu programming/AI.

## Schema đề xuất cho mỗi mẫu

```yaml
id: unique-id
title: "Tên bài"
language: python
topic: algorithms
difficulty: medium
type: problem|lesson|exercise|solution|test
source_url: "https://..."
license: "..."
redistribution_allowed: true|false
ai_training_allowed: true|false
statement: "..."
input_format: "..."
output_format: "..."
examples: []
tests: []
solution: "..."
```

## Quy tắc thu thập

- Không trùng lặp.
- Ghi nguồn và license cho từng item.
- Chỉ sao chép nội dung khi license/terms cho phép.
- Với tài liệu có bản quyền không cho phép tái phân phối: chỉ lưu metadata + URL + mô tả ngắn.
- Ưu tiên dữ liệu có quyền sử dụng rõ ràng cho machine learning/AI training.
- Giữ problem statement, tests và solutions tách riêng để thuận tiện tạo train/validation/evaluation splits.

## Mục tiêu

- Tổng mục tiêu: **10.000 tài liệu/bài tập distinct**.
- Ưu tiên chất lượng và tính hợp pháp hơn số lượng.
- Theo dõi provenance để có thể loại bỏ nguồn khi license thay đổi.
