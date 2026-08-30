# Khương — Roadmap

> Repo mới. Roadmap này mô tả thứ tự phát triển dự kiến; **chưa có giai đoạn nào được coi là hoàn thành**.

| Giai đoạn | Nội dung | Trạng thái |
|---|---|---|
| 1 | Hiện trạng + kiến trúc + contracts | ⬜ Chưa làm |
| 2 | Runtime, dependency, tooling, platform | ⬜ Chưa làm |
| 3 | Model + tokenizer + integration | ⬜ Chưa làm |
| 4 | Dataset + training + checkpoint | ⬜ Chưa làm |
| 5 | Artifact + inference runtime | ⬜ Chưa làm |
| 6 | Local API + UI + entry point | ⬜ Chưa làm |
| 7 | Reasoning + verification | ⬜ Chưa làm |
| 8 | State + context + planning | ⬜ Chưa làm |
| 9 | Memory + knowledge + world model | ⬜ Chưa làm |
| 10 | Mission + agent + tools + skills | ⬜ Chưa làm |
| 11 | Experiment + failure recovery + lessons | ⬜ Chưa làm |
| 12 | Evaluation + observability + self-improvement | ⬜ Chưa làm |
| 13 | Model routing + local-first optimization | ⬜ Chưa làm |
| 14 | Integration toàn hệ thống | ⬜ Chưa làm |
| 15 | Product testing + packaging + release | ⬜ Chưa làm |

## Thứ tự ưu tiên

```text
Kiến trúc
  ↓
Nền tảng
  ↓
Model + Tokenizer
  ↓
Dataset + Training
  ↓
Artifact + Runtime
  ↓
API + UI
  ↓
Reasoning + Verification
  ↓
State + Planning
  ↓
Memory + Knowledge
  ↓
Agent + Tools
  ↓
Recovery + Evaluation
  ↓
Routing + Optimization
  ↓
Integration
  ↓
Product release
```

## Điều kiện chuyển giai đoạn

Không chuyển sang giai đoạn sau chỉ vì đã viết code. Giai đoạn trước phải có implementation thực tế, test/verification và evidence phù hợp. Nếu phát hiện regression hoặc lỗi quan trọng, phải quay lại giai đoạn liên quan để sửa.

## Mục tiêu sản phẩm

Đích cuối là một hệ thống AI local-first có thể nhận mục tiêu dài, lập kế hoạch, sử dụng công cụ, ghi nhớ trạng thái, kiểm chứng kết quả, phục hồi khi thất bại và hoàn thành mission nhiều bước.

**Trạng thái roadmap: ⬜ Chưa triển khai.**
