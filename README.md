# Khương

> **Khương là một dự án AI local-first đang được bắt đầu xây dựng.**
>
> Mục tiêu là phát triển từ một model khoảng 1B tham số thành một hệ thống AI có khả năng suy luận, lập kế hoạch, ghi nhớ, sử dụng công cụ, kiểm chứng và hoàn thành nhiệm vụ nhiều bước.

## Trạng thái hiện tại

Repository này là **repo mới**. Chưa có implementation production nào được xác nhận hoàn thành.

Các phần dưới đây là **mục tiêu và kế hoạch**, không phải tuyên bố rằng chúng đã được xây dựng.

## Khương là gì?

Khương không chỉ hướng tới chatbot hỏi–đáp. Mục tiêu của hệ thống là:

`Goal → Plan → Action → Observation → Verification → State update → Next action`

Khi hoàn thiện, Khương có thể nhận một mục tiêu, phân rã thành nhiệm vụ, thực hiện, kiểm tra kết quả, sửa lỗi và tiếp tục cho tới khi hoàn thành.

## Kiến trúc mục tiêu

Khương dự kiến gồm các lớp:

- Model
- Tokenizer
- Runtime / Inference
- Reasoning
- Planning
- State / Context
- Memory
- Knowledge
- Agent
- Tools / Skills
- Verification
- Recovery
- Evaluation
- API / UI

Các lớp sẽ được thiết kế có boundary rõ ràng để có thể thay đổi model, backend, device hoặc runtime mà không phải viết lại toàn bộ hệ thống.

## Model mục tiêu

- Model: khoảng 1B tham số
- Kiến trúc: decoder-only Transformer
- Vocab mục tiêu: 131072
- Context mục tiêu: 4096
- Layers mục tiêu: 24
- Hidden size mục tiêu: 2048
- Attention heads mục tiêu: 16
- KV heads mục tiêu: 8
- FFN hidden mục tiêu: 3072
- Positional encoding: RoPE
- Normalization: RMSNorm
- Activation: SwiGLU
- Output head: tied với embedding
- Tokenizer mục tiêu: byte-level BPE

Đây chỉ là **cấu hình mục tiêu**, chưa phải bằng chứng model production đã tồn tại hoặc đã được training.

## Mục tiêu hệ thống

### Reasoning
Suy luận nhiều bước, duy trì trạng thái trung gian và có tiêu chí dừng.

### Verification
Kiểm tra kết quả bằng evidence, expected result hoặc tool phù hợp; có khả năng sửa và chạy lại khi phát hiện lỗi.

### Memory
Hướng tới working, episodic, semantic và project memory để lưu và tái sử dụng thông tin lâu dài.

### Mission
Xử lý công việc dài theo vòng đời:

`Create → Plan → Execute → Pause/Resume → Verify → Complete/Recover`

### Tools và coding
Có thể mở rộng tới file, project, terminal, coding, web và computer actions thông qua capability/tool layer.

### Self-improvement
Mọi thay đổi quan trọng phải được đánh giá trước/sau, có regression gate và chỉ giữ lại khi evidence cho thấy cải thiện.

### Local-first
Ưu tiên chạy local, có khả năng thích nghi theo CPU/GPU/RAM/VRAM, dtype, quantization, offload và fallback.

## Nguyên tắc phát triển

1. Xây thật trước khi đánh dấu hoàn thành.
2. Không coi tài liệu hoặc skeleton là implementation.
3. Mỗi module phải có test phù hợp.
4. Mỗi integration quan trọng phải có integration test/evidence.
5. Phát hiện lỗi ở phần đã hoàn thành thì mở lại và sửa.
6. Không tạo implementation trùng với canonical architecture.
7. Ưu tiên reproducibility và evidence.

## Tài liệu

- `README.md` — tổng quan dự án.
- `README-huongtoi.md` — mục tiêu cuối cùng.
- `README-nhiemvu.md` — cây nhiệm vụ kỹ thuật.
- `ROADMAP.md` — roadmap và trạng thái theo giai đoạn.

**Trạng thái hiện tại: Chưa triển khai / đang chuẩn bị nền tảng.**
