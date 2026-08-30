# Free AI API Agent

## Mục tiêu
Tự động tìm, kiểm tra và chọn API AI miễn phí hoặc có free tier để thay thế provider/agent hết quota.

## Nguyên tắc
- Chỉ dùng API/provider có điều khoản sử dụng rõ ràng.
- Không hard-code API key vào repository.
- Ưu tiên provider có API tương thích OpenAI hoặc adapter dễ tích hợp.
- Kiểm tra quota, rate limit, model availability, latency và trạng thái HTTP trước khi chọn.
- Khi provider hết quota/lỗi liên tục, tự đánh dấu unhealthy và chuyển sang provider dự phòng.
- Không tự ý vượt rate limit, CAPTCHA, paywall hoặc cơ chế giới hạn.

## Pipeline
1. Discover: tìm provider/API từ nguồn công khai đáng tin cậy.
2. Verify: kiểm tra documentation, model, free tier và endpoint.
3. Health check: gọi endpoint kiểm tra an toàn, không gửi dữ liệu nhạy cảm.
4. Score: xếp hạng theo khả dụng, quota, độ trễ, context và chi phí.
5. Route: chọn provider tốt nhất cho agent.
6. Failover: chuyển sang provider tiếp theo khi quota hoặc endpoint thất bại.
7. Record: lưu provider, model, thời điểm kiểm tra, trạng thái và provenance.

## Cấu hình logic
```yaml
providers:
  - name: provider_a
    endpoint: ENV
    api_key: ENV
    enabled: true
    priority: 1
  - name: provider_b
    endpoint: ENV
    api_key: ENV
    enabled: true
    priority: 2
routing:
  retry_on: [429, 500, 502, 503, 504]
  max_retries: 2
  cooldown_seconds: 60
```

## Không làm
- Không thu thập hoặc lưu API key của người khác.
- Không tự động đăng ký hàng loạt tài khoản để né giới hạn.
- Không tuyên bố một API là miễn phí nếu chưa xác minh.
