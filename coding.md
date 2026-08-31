# Tài liệu học Coding

> Kho học coding theo hướng **nền tảng CS → ngôn ngữ → thuật toán → Git → data → ML → project**. Mỗi nguồn bên dưới có mô tả nội dung, cách học và bài tập gợi ý; không chỉ lưu tiêu đề.

## 1. Computer Science và tư duy lập trình

### Harvard CS50 — Introduction to Computer Science
- Phù hợp để xây nền tảng trước khi chuyên sâu một stack.
- Nội dung gồm computational thinking, abstraction, algorithms, data structures, correctness, design và style.
- Khóa học bắt đầu bằng C để hiểu memory và cách máy tính vận hành ở mức thấp; sau đó chuyển sang Python, SQL, HTML, CSS và JavaScript.
- Có problem sets và final project nên phù hợp với cách học project-based.
- Nguồn: https://cs50.harvard.edu/college/2026/fall/syllabus/

### Khan Academy — Algorithms
- Tập trung vào searching, sorting, recursion và graph theory.
- Có visualization, articles, quizzes và programming challenges.
- Nên dùng để hình thành trực giác thuật toán trước khi chuyển sang giải bài bằng code.
- Nguồn: https://www.khanacademy.org/computing/intro-to-algorithms

## 2. Python

### Python Documentation
- Tutorial chính thức cho syntax và các tính năng cốt lõi.
- Library Reference để tra standard library và built-ins.
- Language Reference để hiểu chính xác syntax/semantics.
- HOWTOs dành cho các chủ đề chuyên sâu.
- Nguồn: https://docs.python.org/3.14/

### Checklist Python
1. Variables, numbers, strings, booleans.
2. `if/elif/else`, `for`, `while`.
3. Functions, arguments, return values và scope.
4. List, tuple, set, dictionary.
5. Comprehensions.
6. Exceptions và logging.
7. Modules, packages, virtual environments.
8. File I/O, JSON, CSV.
9. OOP, composition và dataclasses.
10. Type hints.
11. Unit testing.
12. Packaging và dependency management.

### Project luyện tập
- CLI calculator.
- File organizer.
- CSV/JSON cleaner.
- REST API client.
- Web scraper có retry, rate limit và logging.
- Một project cuối khóa có test + README + Git history.

## 3. JavaScript và Web

### MDN JavaScript Guide
Guide bao phủ introduction, grammar/types, control flow, loops, functions, expressions/operators, numbers/strings, dates, regex, collections, objects, classes, promises, iterators/generators, resource management, internationalization và modules.

- Guide: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide
- Reference: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference

### Checklist JavaScript
- Scope, `let`/`const`.
- Functions và closures.
- Objects, prototypes, classes.
- Arrays và collections.
- Error handling.
- Promise + `async/await`.
- Modules.
- DOM.
- Fetch/HTTP/JSON.
- Browser storage và Web APIs.

## 4. Git và GitHub

### Pro Git Book
Tài liệu bao phủ version control, repository, commit history, undo, remotes, tags, branches, merging, rebasing, distributed workflows, GitHub và Git tooling.

- Nguồn: https://git-scm.com/book/en/v2
- License của sách: Creative Commons Attribution-NonCommercial-ShareAlike 3.0.

### Workflow thực hành
```text
git clone
→ branch
→ code
→ test
→ git diff
→ git add
→ git commit
→ git push
→ Pull Request
→ review
→ merge
```

Không nên chỉ học command. Cần hiểu commit graph, branch, merge/rebase, remote tracking và cách phục hồi thay đổi.

## 5. NumPy

### NumPy User Guide
NumPy là nền tảng scientific computing trong Python. User Guide tập trung vào ndarray, array creation, indexing, I/O, dtypes, broadcasting, copies/views, string/structured arrays và interoperability.

- Nguồn: https://numpy.org/doc/stable/user/

### Bài tập
- Tạo và reshape arrays.
- Vectorization thay cho Python loop khi phù hợp.
- Broadcasting.
- Tính mean/std/percentile.
- Matrix operations.
- Đọc và ghi dữ liệu số.

## 6. pandas và xử lý dữ liệu

### pandas Getting Started + User Guide
pandas cung cấp DataFrame và công cụ để explore, clean và process dữ liệu dạng bảng. Tài liệu chính thức có hướng dẫn CSV, Excel, SQL, JSON, Parquet, selection, missing data, groupby, reshape, plotting và time series.

- Getting started: https://pandas.pydata.org/docs/getting_started/
- User Guide: https://pandas.pydata.org/docs/user_guide/

### Pipeline nên luyện
```text
Raw data
  ↓
Load
  ↓
Validate schema
  ↓
Handle missing/duplicates
  ↓
Normalize types
  ↓
Feature engineering
  ↓
Aggregate / join / reshape
  ↓
Analysis
  ↓
Export
```

Project tốt để luyện: lấy một dataset có timestamp, xây pipeline làm sạch và tạo báo cáo thống kê có thể chạy lại.

## 7. Machine Learning

### scikit-learn User Guide
- Bao phủ supervised learning, linear models, logistic regression, SVM, dimensionality reduction và nhiều thuật toán ML thực dụng.
- Nguồn: https://scikit-learn.org/stable/user_guide.html

### Kiến thức bắt buộc
- Train/validation/test split.
- Baseline.
- Cross-validation.
- Feature engineering.
- Data leakage.
- Overfitting/underfitting.
- Classification metrics: precision, recall, F1, ROC-AUC.
- Regression metrics.
- Hyperparameter tuning.
- Reproducibility.

## 8. Coding cho AI / agent

Khi dùng coding để xây AI agent, nên bổ sung:
- API design và JSON schema.
- Tool/function calling.
- Retry, timeout và idempotency.
- Logging và tracing.
- Evaluation dataset.
- Unit/integration tests.
- Sandboxing cho code execution.
- Git-based versioning.
- Regression tests trước/sau khi AI sửa code.

AI coding nên được dùng như một **pair programmer**: yêu cầu giải thích, tạo test, review và đề xuất phương án; code phải được chạy và kiểm chứng độc lập.

## 9. Lộ trình tổng hợp

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
Web/backend hoặc systems
        ↓
scikit-learn / AI
        ↓
Project thực tế + portfolio
```

## 10. Danh mục nguồn

| Chủ đề | Nguồn | Nội dung chính |
|---|---|---|
| Computer Science | Harvard CS50 | Problem solving, C, Python, SQL, web |
| Algorithms | Khan Academy | Search, sort, recursion, graphs |
| Python | Python Docs | Syntax, standard library, HOWTO |
| JavaScript | MDN | Guide + reference |
| Version control | Pro Git | Git/GitHub workflow |
| Numerical computing | NumPy | Arrays, broadcasting, numerical operations |
| Data analysis | pandas | DataFrame, cleaning, time series |
| ML | scikit-learn | Supervised learning và model evaluation |

## 11. Bản quyền và cách sử dụng

File này là **bản tổng hợp/ghi chú**, không sao chép toàn văn các khóa học, sách hoặc tài liệu nguồn. Khi đưa dữ liệu vào corpus training AI, cần kiểm tra license/terms và provenance của từng nguồn. Với tài liệu không cho phép tái phân phối, chỉ nên lưu metadata, tóm tắt và URL nguồn.

## 12. Nguồn đã kiểm chứng

- Python Docs: https://docs.python.org/3.14/
- Harvard CS50: https://cs50.harvard.edu/college/2026/fall/syllabus/
- Khan Academy Algorithms: https://www.khanacademy.org/computing/intro-to-algorithms
- MDN JavaScript Guide: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide
- Pro Git: https://git-scm.com/book/en/v2
- NumPy User Guide: https://numpy.org/doc/stable/user/
- pandas: https://pandas.pydata.org/docs/getting_started/
- scikit-learn: https://scikit-learn.org/stable/user_guide.html
