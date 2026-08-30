# Khương — Nhiệm vụ phát triển

## Quy tắc

1. Làm theo thứ tự từ trên xuống dưới.
2. Mục chưa có implementation và evidence phải giữ trạng thái `⬜ Chưa làm`.
3. Không đánh dấu hoàn thành chỉ vì có ý tưởng, tài liệu hoặc skeleton.
4. Khi hoàn thành một mục phải test/verification ít nhất 2 lượt, ghi evidence và cập nhật trạng thái.
5. Nếu phát hiện lỗi ở mục đã hoàn thành, mở lại và sửa.
6. Không tạo implementation trùng với kiến trúc canonical.
7. Ưu tiên code chạy được, test và evidence.

## Trạng thái

- ⬜ Chưa làm
- 🟡 Đang làm
- 🟢 ĐÃ XONG
- 🔴 Có lỗi cần mở lại
- ⚪ Bị chặn / cần điều kiện bên ngoài

## GIAI ĐOẠN 1 — Kiến trúc và hiện trạng

### 1.1 Hiểu mục tiêu — 🟢 ĐÃ XONG
- Đọc toàn bộ tài liệu dự án.
- Chốt mục tiêu hệ thống.
- Chốt model mục tiêu.
- Evidence: `README.md`, `README-huongtoi.md`, `ROADMAP.md` đã được rà soát.

### 1.2 Quét repository — 🟢 ĐÃ XONG
- Kiểm kê file/thư mục.
- Xác định implementation hiện có.
- Xác định phần thiếu.
- Evidence: repository hiện không có production implementation; đã thiết lập các vùng `src/`, `tests/`, `configs/`, `scripts/`, `docs/`.

### 1.3 Khóa kiến trúc — 🟢 ĐÃ XONG
- Model/tokenizer/runtime boundary.
- Orchestration boundary.
- Dependency direction.
- Artifact contract.
- Evidence: `docs/ARCHITECTURE.md`.

### 1.4 Model ↔ runtime contract — 🟢 ĐÃ XONG
- Input/output contract.
- Tokenizer contract.
- Artifact validation.
- Compatibility metadata.
- Implementation: `src/khuong/contracts.py`, `src/khuong/runtime.py`.
- Verification: 7 tests PASS trên VPS Python 3.12; GitHub Actions cũng đã PASS.
- Evidence: `tests/test_contracts.py`, `tests/test_runtime.py`, CI workflow.

## GIAI ĐOẠN 2 — Nền tảng

### 2.1 Runtime/dependency — 🟡 Đang làm
- Python/runtime.
- Dependency.
- CPU/GPU/CUDA.
- Environment sạch.
- Install/test/run commands.

### 2.2 Tooling — ⬜ Chưa làm
- Terminal.
- File/project utilities.
- Search/diff.
- Test runner.
- Benchmark.
- Logging/trace.

### 2.3 Platform verification — ⬜ Chưa làm
- Smoke test.
- Clean-install verification.
- Hardware/runtime evidence.

## GIAI ĐOẠN 3 — Model và Tokenizer

### 3.1 Model — ⬜ Chưa làm
- `model/model.py`.
- Config validation.
- Module/shape checks.
- Forward.
- Decode/KV cache.
- Unit tests.

### 3.2 Tokenizer — ⬜ Chưa làm
- `model/tokenizer.py`.
- Encode/decode.
- Special tokens.
- Corpus.
- Production tokenizer.
- Vocab 131072.
- Việt/Anh/Unicode.
- Artifact + metadata.

### 3.3 Integration — ⬜ Chưa làm
- Vocab/special IDs.
- Token range.
- Text → IDs → model → IDs → text.

## GIAI ĐOẠN 4 — Dataset, Training, Checkpoint

### 4.1 Dataset — ⬜ Chưa làm
Source, license/provenance, ingest, clean, deduplicate, quality filter, split, leakage check, tokenize.

### 4.2 Training — ⬜ Chưa làm
Data loader, packing, masks, causal LM labels, loss, optimizer, scheduler, gradient handling, dtype/AMP, logging, NaN/Inf detection, overfit test, smoke training.

### 4.3 Checkpoint — ⬜ Chưa làm
Save/load, resume, metadata, hash, validation.

### 4.4 Training thật — ⬜ Chưa làm
Hyperparameters, pilot, resource monitoring, training, validation, checkpoint selection, reproducibility.

## GIAI ĐOẠN 5 — Artifact và Runtime

### 5.1 Artifact bundle — ⬜ Chưa làm
Weights, config, tokenizer, runtime config, metadata, version, checksum, manifest.

### 5.2 Runtime — ⬜ Chưa làm
Manifest validation, loading, device selection, prefill/decode, KV cache, sampling, stop conditions, context, streaming, error/resource handling.

### 5.3 CPU/GPU — ⬜ Chưa làm
CPU, CUDA, VRAM check, offload, quantization, benchmark.

## GIAI ĐOẠN 6 — API và UI — ⬜ Chưa làm

Health, chat, streaming, validation, timeout, error handling, UI, conversation state, E2E và một lệnh chạy.

## GIAI ĐOẠN 7 — Reasoning và Verification — ⬜ Chưa làm

Golden tasks, multi-step reasoning, stop criteria, verification, correction/re-run, uncertainty states, multi-path, scoring, pruning, backtracking.

## GIAI ĐOẠN 8 — State, Context và Planning — ⬜ Chưa làm

User/project/mission/task/environment/tool state; persistence; context budget; relevance; retrieval; compaction; goals; constraints; priority; decomposition; dependencies; replanning; recovery.

## GIAI ĐOẠN 9 — Memory, Knowledge và World Model — ⬜ Chưa làm

Working/episodic/semantic/project memory; capture/store/retrieve/rank; consolidation; conflict/stale detection; entities/relations/events/state/time; knowledge acquisition; provenance/evidence.

## GIAI ĐOẠN 10 — Mission, Agent và Tools — ⬜ Chưa làm

Mission lifecycle; planner; executor; observer; verifier; memory/tool/skill/recovery managers; terminal/file/project/coding/browser/computer tools; governance; capability registry.

## GIAI ĐOẠN 11 — Experiment và Recovery — ⬜ Chưa làm

Hypothesis, variables, expected result, execution, observation, comparison, root cause, retry, alternative tool/plan, rollback, recovery verification, lessons, regression tests.

## GIAI ĐOẠN 12 — Evaluation và Self-improvement — ⬜ Chưa làm

Golden tasks, metrics, regression gates, traces, replay, before/after benchmarks, quality/latency/resource comparison, keep/revert by evidence.

## GIAI ĐOẠN 13 — Model Routing và Local-first — ⬜ Chưa làm

Capability registry, task classification, model selection, scoring, fallback, provider adapter, hardware detection, dtype, quantization, offload, benchmark, OOM recovery.

## GIAI ĐOẠN 14 — Integration toàn hệ thống — ⬜ Chưa làm

Model ↔ tokenizer ↔ runtime ↔ state/context ↔ memory ↔ reasoning ↔ planning ↔ agent ↔ tools/skills ↔ verification/evaluation ↔ recovery ↔ API/UI.

## GIAI ĐOẠN 15 — Kiểm thử thành phẩm và release — ⬜ Chưa làm

Unit, integration, E2E, recovery, performance, regression, clean-machine, packaging và release verification.

**Trạng thái hiện tại: Giai đoạn 2 đang thực hiện mục 2.1; chưa được phép chuyển sang 2.2 khi 2.1 chưa có evidence đầy đủ.**
