# Free API Search Agent

## Mục tiêu
Tự động tìm các API AI miễn phí hoặc có free tier hợp lệ để bổ sung pool cho Khương.

## Pipeline
1. Tìm provider từ nguồn công khai đáng tin cậy.
2. Kiểm tra documentation và endpoint.
3. Xác minh free tier/quota/rate limit tại thời điểm kiểm tra.
4. Kiểm tra model và khả năng dùng cho coding/reasoning/general.
5. Health-check nếu endpoint công khai cho phép.
6. Xếp hạng provider theo quota, chất lượng model, tốc độ và độ ổn định.
7. Xuất danh sách provider cho Free AI API Agent/Router.

## Chính sách
- Free tier phải được xác minh, không suy đoán.
- Ghi thời điểm kiểm tra vì chính sách/quota có thể thay đổi.
- Không tự động tạo hàng loạt tài khoản.
- Không né rate limit, CAPTCHA hoặc giới hạn của nhà cung cấp.
- Không lưu API key thật trong GitHub.
- Chỉ dùng key được cung cấp hợp pháp qua environment/secret manager.

## Đầu ra
```json
{"provider":"...","model":"...","endpoint":"...","free_tier":"...","rate_limit":"...","checked_at":"...","source":"...","status":"verified|unknown|unavailable"}
```
