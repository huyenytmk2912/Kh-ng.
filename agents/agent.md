# 🤖 Bản đồ Agent Khương

## Quy ước
Các agent được đánh số để dễ gọi và theo dõi. Mỗi agent có một nhiệm vụ chính; Orchestrator điều phối chúng.

| Số | Tên | Nhiệm vụ |
|---|---|---|
| 🤔1 | Điều phối | Phân công và nối toàn bộ pipeline |
| 🔎2 | Internet | Tìm tài liệu trên Internet |
| 🆓3 | Free API | Tìm API AI miễn phí/free tier |
| 🖥️4 | Local AI | Quản lý model local → API |
| 📚5 | Coding Search | Tìm tài liệu coding |
| 🧠6 | Tư duy Search | Tìm tài liệu tư duy/reasoning |
| 📥7 | Collector | Thu thập nội dung được phép |
| 🇻🇳8 | Việt hóa | Chuyển nội dung sang tiếng Việt |
| 🧪9 | Coding Data | Tạo dữ liệu training coding |
| 💭10 | Tư duy Data | Tạo dữ liệu training tư duy |
| 🔍11 | Reviewer Coding | Soát dữ liệu coding lần 1 |
| 🔬12 | Reviewer Tư duy | Soát dữ liệu tư duy lần 1 |
| 🛡️13 | Final Validator | Soát cuối trước dataset |
| ♻️14 | Dedup | Loại dữ liệu trùng |
| 🗂️15 | Dataset | Đóng gói/version dataset |
| 🏋️16 | Trainer | Đưa dataset vào training |
| 📊17 | Evaluator | Đánh giá model sau training |
| 🔀18 | API Router | Chọn local/cloud provider |
| ❤️19 | Health Monitor | Theo dõi model/API |
| 🔐20 | Security | Kiểm tra secret và an toàn |
| ⏱️21 | Scheduler | Điều phối tác vụ tự động |
| 💾22 | Backup | Sao lưu dataset/model/config |
| 📝23 | Documentation | Cập nhật tài liệu dự án |
| 🚀24 | Deploy | Đóng gói và triển khai |

## Pipeline dữ liệu chuẩn
`2/5/6 → 7 → 8 → 9/10 → 11/12 → 13 → 14 → 15 → 16 → 17`

Không đưa dữ liệu vào training nếu chưa qua reviewer và final validator.

## Local model đề xuất
Với VPS khoảng 20 GB RAM, ưu tiên **Qwen3-Coder 14B Q4/Q5** cho coding và tạo dữ liệu. Q4 cần khoảng 10–12 GB tùy runtime/context, nên vẫn phải chừa RAM cho hệ điều hành và dịch vụ. Nếu VPS chỉ có CPU, vẫn chạy được nhưng tốc độ sẽ thấp. Các nguồn benchmark hiện tại cũng xếp Qwen coder 14B vào nhóm phù hợp cho phần cứng 12–16 GB; không nên nhảy thẳng lên model 30B khi chưa kiểm tra RAM/VRAM thực tế. citeturn0search2turn0search4

Model local chỉ tạo bản nháp. Dữ liệu phải qua **🤔1 → 🧪9/💭10 → 🔍11/12 → 🛡️13** trước khi thành training data.
