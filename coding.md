# Tài liệu học Coding + AI Coding

> Bộ tài liệu học theo hướng **Computer Science → Python → Git → data → ML → AI engineering → project**. Đây là bản tổng hợp/ghi chú có nội dung học, bài tập và nguồn gốc; không sao chép toàn văn tài liệu bên ngoài.

## 1. Computer Science nền tảng

### Harvard CS50 — Introduction to Computer Science
CS50 phù hợp để xây tư duy giải quyết vấn đề trước khi chạy theo framework. Chương trình 2026 mô tả computational thinking, abstraction, algorithms, data structures, correctness, design và style. Khóa bắt đầu bằng C để hiểu memory và máy tính ở mức thấp, sau đó chuyển sang Python, SQL, HTML, CSS và JavaScript; cuối khóa có final project.

**Cách học:** làm problem set trước khi xem lời giải; ghi lại cách tiếp cận, complexity và lỗi gặp phải.

- Nguồn: https://cs50.harvard.edu/college/2026/fall/syllabus/

### Thuật toán và cấu trúc dữ liệu
Cần nắm Big-O, arrays, linked lists, stacks, queues, hash tables, trees, heaps, graphs, searching, sorting, recursion, dynamic programming, BFS/DFS và shortest path.

**Bài tập:** mỗi thuật toán phải có implementation, test cases, complexity analysis và ít nhất một failure/edge case.

## 2. Python

### Python Tutorial — Python 3.14
Tutorial chính thức tập trung vào người đã có chút nền tảng lập trình và muốn học Python. Nội dung gồm interpreter, numbers/text/lists, control flow, functions, data structures, modules, I/O, errors/exceptions, classes, standard library và virtual environments/packages.

- Nguồn: https://docs.python.org/3.14/tutorial/

### Checklist Python
1. Variables, numbers, strings, booleans.
2. `if`, `for`, `while`, `match`.
3. Functions, arguments, scope.
4. List/tuple/set/dict.
5. Comprehensions và generators.
6. Exceptions, logging.
7. Modules/packages.
8. `venv`, dependency management.
9. File I/O, JSON, CSV.
10. OOP, composition, dataclasses.
11. Type hints.
12. Unit/integration testing.
13. Async basics khi làm I/O-heavy systems.

### Project luyện tập
- CLI calculator.
- File organizer.
- CSV/JSON cleaner.
- REST API client có retry/timeout.
- Web scraper có rate limit và logging.
- Project cuối khóa có tests, README, CI và Git history sạch.

## 3. JavaScript / Web

### MDN JavaScript Guide
MDN Guide bao phủ grammar/types, control flow, loops, functions, expressions/operators, numbers/strings, dates, regex, collections, objects, classes, promises, iterators/generators, internationalization và modules. Reference dùng để tra chi tiết từng language feature.

- Guide: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide
- Reference: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference

### Checklist
- Scope và `let`/`const`.
- Functions, closures.
- Objects/prototypes/classes.
- Arrays/Map/Set.
- Error handling.
- Promise + `async/await`.
- Modules.
- DOM và browser APIs.
- Fetch/HTTP/JSON.
- Basic Node.js/backend concepts.

## 4. Git và GitHub

### Pro Git
Pro Git bao phủ version control, repository, commit history, branching, merging, rebasing, remotes, tags và distributed workflows. Git cũng có tài liệu Learn với video và cheat sheet cho người mới.

- Pro Git: https://git-scm.com/book/en/v2
- Git Learn: https://git-scm.com/learn

### Workflow thực hành
```text
git clone → branch → code → test → git diff → git add → git commit
→ git push → Pull Request → review → merge
```

Không chỉ học command. Cần hiểu commit graph, remote tracking, merge/rebase, revert/reset và cách phục hồi thay đổi.

## 5. Numerical + Data stack

### NumPy
NumPy là nền tảng scientific computing trong Python, cung cấp multidimensional arrays, indexing, broadcasting, numerical/statistical operations, linear algebra và random simulation.

- User Guide: https://numpy.org/doc/stable/user/

**Bài tập:** reshape, indexing, broadcasting, vectorization, mean/std/percentile, matrix operations, random simulation.

### pandas
pandas tập trung vào dữ liệu dạng bảng và time series. User Guide có DataFrame/Series, missing data, selection, merge, groupby, reshape, plotting, importing/exporting và time series.

- User Guide: https://pandas.pydata.org/docs/user_guide/
- 10 minutes to pandas: https://pandas.pydata.org/docs/getting_started/intro_tutorials/

**Pipeline:** Raw data → schema validation → clean → normalize types → feature engineering → join/reshape → analysis → export.

## 6. Machine Learning

### scikit-learn User Guide
Tài liệu hiện tại bao phủ supervised/unsupervised learning, preprocessing, pipelines, model persistence và common pitfalls. Đặc biệt cần học data leakage, inconsistent preprocessing và cách chọn estimator.

- Nguồn: https://scikit-learn.org/stable/user_guide.html

### Kiến thức bắt buộc
- Train/validation/test split.
- Baseline và cross-validation.
- Feature engineering.
- Data leakage.
- Overfitting/underfitting.
- Classification/regression metrics.
- Hyperparameter tuning.
- Reproducibility.
- Pipeline để tránh preprocessing leakage.

## 7. Coding cho AI / AI agents

Coding AI không chỉ là viết prompt. Cần có engineering loop:

```text
Requirement → Design/interface → Implementation → Tests
→ Run/observe → Evaluate → Review → Commit
```

### Các năng lực nên học
- Python + HTTP/API + JSON schema.
- Tool/function calling.
- Structured outputs và validation.
- Retry, timeout, idempotency.
- Logging, tracing và observability.
- Unit/integration/evaluation tests.
- Dataset cho regression/evaluation.
- Sandboxing khi cho model chạy code.
- Secret management; không hard-code API keys.
- Git-based versioning và CI.

### AI pair-programming workflow
1. Mô tả requirement và acceptance criteria.
2. Yêu cầu AI lập plan trước khi sửa nhiều file.
3. Tạo implementation nhỏ, có test.
4. Chạy test/linter/type checker độc lập.
5. Review diff thay vì tin output nguyên trạng.
6. Ghi failure cases thành regression tests.
7. Commit thay đổi nhỏ, message rõ ràng.

**Nguyên tắc:** AI tạo code không đồng nghĩa code đã đúng. Behavior phải được kiểm chứng bằng tests, execution và review.

## 8. Project portfolio

### Project A — Data pipeline
CSV/API → validation → cleaning → pandas analysis → report → tests → GitHub.

### Project B — AI API service
HTTP service → schema validation → model/API call → retry/timeout → logging → tests → deployment notes.

### Project C — Coding agent
Agent nhận issue, đọc repository, đề xuất plan, sửa code, chạy tests và tạo patch/PR. Phải có sandbox, tool permissions và evaluation set.

### Project D — ML project
Dataset → baseline → preprocessing pipeline → model → cross-validation → error analysis → model card/README.

## 9. Lộ trình đề xuất

```text
CS50 / Algorithms
        ↓
Python fundamentals
        ↓
Git + GitHub
        ↓
Data structures + algorithms
        ↓
NumPy + pandas + SQL
        ↓
Testing + clean code
        ↓
Backend / APIs
        ↓
ML fundamentals
        ↓
AI engineering / agents
        ↓
Project thực tế + portfolio
```

## 10. Nguồn chính đã kiểm chứng

| Chủ đề | Nguồn | Nội dung |
|---|---|---|
| Computer Science | Harvard CS50 | C, Python, SQL, algorithms, data structures, web |
| Python | Python Docs 3.14 | Tutorial + language ecosystem |
| JavaScript | MDN | Guide + reference |
| Version control | Pro Git | Git workflow và internals |
| Numerical computing | NumPy | Arrays, broadcasting, numerical computing |
| Data analysis | pandas | DataFrame, cleaning, time series |
| ML | scikit-learn | Models, pipelines, evaluation, leakage |

## 11. Bản quyền / provenance

Chỉ lưu **tóm tắt, ghi chú và metadata** của tài liệu nguồn. Không sao chép toàn văn sách/khóa học không cho phép tái phân phối. Nếu dùng các ghi chú này để xây corpus/training AI, cần kiểm tra license, terms, provenance và quyền sử dụng của từng nguồn.

## 12. Cập nhật nguồn

- Harvard CS50 syllabus 2026: https://cs50.harvard.edu/college/2026/fall/syllabus/
- Python Tutorial 3.14: https://docs.python.org/3.14/tutorial/
- MDN JavaScript Guide: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide
- Pro Git: https://git-scm.com/book/en/v2
- NumPy User Guide: https://numpy.org/doc/stable/user/
- pandas User Guide: https://pandas.pydata.org/docs/user_guide/
- scikit-learn User Guide: https://scikit-learn.org/stable/user_guide.html
