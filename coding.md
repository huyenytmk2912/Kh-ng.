# Tài liệu học Coding + AI Coding

> Curriculum thực hành: Computer Science → Python → Git/GitHub → data → ML → AI coding agents → evaluation → project. Nội dung là ghi chú/tóm tắt và liên kết tới nguồn, không sao chép toàn văn tài liệu có bản quyền.

## 1. Computer Science nền tảng

### Harvard CS50
CS50 xây computational thinking trước framework: abstraction, algorithms, data structures, correctness, design và style. Khóa 2026 đi từ C sang Python, SQL, HTML/CSS và JavaScript, kết thúc bằng project.

**Cách học:** làm problem set trước khi xem lời giải; với mỗi bài ghi algorithm, complexity, edge cases và failure mode.

Nguồn: https://cs50.harvard.edu/college/2026/fall/syllabus/

### Algorithms & Data Structures
Cần nắm Big-O, arrays, linked lists, stacks, queues, hash tables, trees, heaps, graphs, sorting/searching, recursion, dynamic programming, BFS/DFS và shortest path.

**Bài tập chuẩn:** implementation + unit tests + complexity analysis + ít nhất một edge case.

## 2. Python

### Python 3.14 Tutorial
Học interpreter, numbers/text/lists, control flow, functions, data structures, modules, I/O, exceptions, classes, standard library và virtual environments/packages.

Nguồn: https://docs.python.org/3.14/tutorial/

**Checklist:** variables → functions → collections → comprehensions/generators → exceptions/logging → modules → venv → JSON/CSV → OOP/composition → type hints → testing → async basics.

**Project:** CLI calculator, file organizer, CSV/JSON cleaner, REST API client có retry/timeout, scraper có rate limit/logging.

## 3. JavaScript / Web

MDN JavaScript Guide bao phủ types, control flow, functions, objects/classes, collections, promises, iterators/generators, modules và browser APIs.

Nguồn: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide
Reference: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference

Học thêm HTTP/JSON, Fetch, DOM, async/await và Node.js fundamentals.

## 4. Git và GitHub

Pro Git giải thích repository, commit history, branches, merging, rebasing, remotes, tags và distributed workflows.

Nguồn: https://git-scm.com/book/en/v2
Git Learn: https://git-scm.com/learn

Workflow:

```text
git clone → branch → code → test → diff → commit
→ push → Pull Request → review → merge
```

Không chỉ nhớ command; phải hiểu commit graph, revert/reset và cách phục hồi thay đổi.

## 5. Numerical + Data

### NumPy
Arrays nhiều chiều, indexing, broadcasting, vectorization, statistics, linear algebra và simulation.
Nguồn: https://numpy.org/doc/stable/user/

### pandas
DataFrame/Series, missing data, selection, merge, groupby, reshape, import/export và time series.
Nguồn: https://pandas.pydata.org/docs/user_guide/

Pipeline nên luyện:

```text
raw data → schema validation → cleaning → type normalization
→ feature engineering → join/reshape → analysis → export
```

## 6. Machine Learning

scikit-learn User Guide bao phủ supervised/unsupervised learning, preprocessing, pipelines, model selection và common pitfalls.
Nguồn: https://scikit-learn.org/stable/user_guide.html

Kiến thức bắt buộc: train/validation/test, cross-validation, baseline, feature engineering, leakage, overfitting/underfitting, metrics, hyperparameter tuning và reproducibility.

Đặc biệt học pipeline để tránh preprocessing leakage và validation phải phù hợp với cấu trúc dữ liệu.

## 7. AI Coding Agents

Coding với AI phải được xem là engineering system, không phải prompt-only workflow:

```text
Requirement → plan → implementation → tests
→ execution → evaluation → review → commit
```

Năng lực nên học:
- Tool/function calling và structured inputs/outputs.
- File/shell/API tools với permission rõ ràng.
- JSON schema, validation, retry, timeout, idempotency.
- Logging, tracing và observability.
- Unit/integration/evaluation tests.
- Sandboxing khi agent chạy code.
- Secret isolation; không hard-code API keys.
- Git-based versioning và CI.

## 8. Hugging Face Agents Course

Khóa học miễn phí/có chứng nhận, đi từ agent fundamentals đến frameworks và triển khai. Nội dung gồm tools, thoughts, actions, observations; sau đó thực hành với smolagents, LangGraph và LlamaIndex, cùng các use case và evaluation.

**Cách học:** viết một agent Python tối giản trước, sau đó dùng framework để so sánh abstraction. Mỗi agent phải có tool, test case và log.

Nguồn: https://huggingface.co/agents-course
Giới thiệu: https://huggingface.co/learn/agents-course/unit0/introduction

## 9. Hugging Face Context Course

Context engineering tập trung vào cách tổ chức kiến thức để agent tìm đúng thông tin đúng lúc. Course hiện có các unit về **Skills, MCP, Plugins, Subagents, Hooks** và một mini agent harness; hỗ trợ Claude Code, Codex và OpenCode.

**Bài tập:** tạo `SKILL.md` cho repository; xây một MCP tool; thêm hook để kiểm soát lifecycle; đo số lỗi/rework trước và sau khi cải thiện context.

Nguồn: https://huggingface.co/context-course
Introduction: https://huggingface.co/learn/context-course/unit0/introduction

## 10. GitHub Copilot Cloud Agent

Copilot cloud agent có thể nghiên cứu repository, lập implementation plan, thay đổi code trên branch, tạo diff và Pull Request. Có thể bắt đầu từ issue hoặc task nhỏ và tiếp tục iterate bằng review comments.

**Bài học:** issue → plan → branch → implementation → tests → diff review → PR. Không coi agent output là đã đúng chỉ vì PR tạo thành công.

Nguồn: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent
Hướng dẫn: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/use-cloud-agent-on-github

### Agent Skills
GitHub mô tả Skills là các thư mục chứa instructions, scripts và resources mà agent nạp khi cần. Có thể tổ chức skill theo project và tái sử dụng giữa các agent.

Nguồn: https://docs.github.com/en/copilot/concepts/agents/about-agent-skills

## 11. OpenAI Codex

Codex hiện được định vị như coding agent cho các task từ pull request, refactor, migration đến công việc dài hạn; Skills có thể truyền workflow và tiêu chuẩn của team cho agent. Đây là tài liệu nên đọc để hiểu agentic software engineering và multi-agent workflows.

Nguồn: https://openai.com/codex/

## 12. Đánh giá coding agent

Không đánh giá bằng “code trông ổn”. Đánh giá bằng behavior có thể kiểm chứng:

- Acceptance criteria.
- Unit/integration tests.
- Regression tests.
- Patch correctness.
- Tool-call errors.
- Retry count.
- Latency và cost/task.
- Security violations.

### SWE-bench Verified
SWE-bench Verified là benchmark gồm 500 task đã được human-validated để đánh giá khả năng giải issue thực tế của coding agents.

Nguồn: https://www.swebench.com/verified.html

**Project benchmark cá nhân:** tạo 20 issue nhỏ → viết acceptance criteria/test → cho agent xử lý → lưu patch + test result + failure category → tính success rate và regression rate.

## 13. AI pair-programming workflow

1. Viết requirement và acceptance criteria.
2. Yêu cầu AI lập plan trước khi sửa nhiều file.
3. Cho agent làm thay đổi nhỏ.
4. Chạy test/linter/type checker độc lập.
5. Review diff, không review chỉ bằng summary.
6. Ghi failure thành regression test.
7. Commit nhỏ, message rõ.

**Nguyên tắc:** model sinh code ≠ code đúng. Correctness phải được chứng minh bằng execution và tests.

## 14. Roadmap học AI coding

```text
CS50 / algorithms
        ↓
Python + Git
        ↓
Testing + clean code
        ↓
APIs + JSON + HTTP
        ↓
NumPy + pandas + SQL
        ↓
ML fundamentals
        ↓
LLM APIs + structured output
        ↓
Tools + agent loop
        ↓
MCP + Skills + context engineering
        ↓
Repository coding agent
        ↓
Evaluation + sandbox + observability
        ↓
Production project
```

## 15. Project portfolio

### Project A — Data pipeline
API/CSV → validation → cleaning → pandas → report → tests → GitHub.

### Project B — AI API service
HTTP endpoint → schema validation → model call → retry/timeout → logging → tests.

### Project C — Repository coding agent
Issue → context → plan → patch → test → review → PR. Agent phải bị giới hạn quyền và có evaluation set.

### Project D — Agent evaluation harness
20–50 task coding có test; chạy nhiều model/agent; lưu trace, patch, test result, cost và failure mode.

## 16. Nguồn cập nhật — 31/08/2026

- Hugging Face Agents Course: https://huggingface.co/agents-course — agent fundamentals, frameworks và evaluation. citeturn0search2
- Hugging Face Context Course: https://huggingface.co/context-course — Skills, MCP, Plugins, Subagents, Hooks và agent harness. citeturn0search0turn0search1
- GitHub Copilot cloud agent: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent — repository research, plan, code changes và PR workflow. citeturn0search13
- GitHub Agent Skills: https://docs.github.com/en/copilot/concepts/agents/about-agent-skills — portable instructions/scripts/resources cho agent. citeturn0search5
- OpenAI Codex: https://openai.com/codex/ — agentic coding, Skills và multi-agent workflows. citeturn0search4
- SWE-bench Verified: https://www.swebench.com/verified.html — benchmark coding agent. 

## 17. Provenance / bản quyền

Chỉ lưu tóm tắt, ghi chú và metadata; không sao chép toàn văn tài liệu không cho phép tái phân phối. Khi dùng tài liệu để xây corpus/training AI, cần kiểm tra license, terms, provenance và quyền sử dụng từng nguồn.