# Local AI API Agent

## Mục tiêu
Biến các model AI chạy local trên VPS thành API nội bộ cho Khương, đồng thời phối hợp với Free AI API Agent để có fallback khi local model hoặc provider bên ngoài không khả dụng.

## Kiến trúc
```text
Client/Agent
    ↓
API Router
    ├── Local Model A
    ├── Local Model B
    ├── Local Model C
    └── Free AI Provider
```

## Nhiệm vụ
1. Phát hiện model/server local đang hoạt động.
2. Kiểm tra health endpoint và latency.
3. Đăng ký model với router bằng tên, endpoint, context limit và trạng thái.
4. Chọn model theo loại tác vụ: coding, reasoning, general.
5. Theo dõi RAM/CPU/GPU nếu có metrics.
6. Khi model lỗi hoặc quá tải, chuyển sang model local khác.
7. Nếu không còn local model khỏe, chuyển sang Free AI API Agent.
8. Khi provider local hoạt động trở lại, đưa nó vào pool.
9. Ghi log routing và lỗi; không ghi prompt chứa dữ liệu nhạy cảm.

## Nguyên tắc tài nguyên VPS
- Không khởi chạy nhiều model lớn đồng thời nếu vượt RAM khả dụng.
- Luôn giữ một phần RAM cho hệ điều hành và các dịch vụ khác.
- Ưu tiên một model ổn định trước khi thêm model thứ hai.
- Không tự ý tải model dung lượng lớn nếu chưa kiểm tra disk/RAM.

## API contract
Ưu tiên API tương thích OpenAI:
- `POST /v1/chat/completions`
- `GET /v1/models`
- `GET /health`

API key của dịch vụ nội bộ, nếu cần, phải lấy từ environment/secret manager, không commit vào GitHub.

## Routing policy
```yaml
routes:
  coding: [local_coding, local_general, free_provider]
  reasoning: [local_reasoning, local_general, free_provider]
  general: [local_general, local_reasoning, free_provider]
health:
  timeout_seconds: 10
  unhealthy_after_failures: 3
```

## An toàn
- Không tự động mở API local ra Internet nếu chưa có authentication/firewall.
- Không lưu API key thật trong repository.
- Không vượt quota của provider bên ngoài.
