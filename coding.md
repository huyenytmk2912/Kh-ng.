# Coding Training Corpus

Mục tiêu: xây dựng kho 10.000 tài liệu/bài tập coding có thể dùng hợp pháp cho việc học và chuẩn bị dữ liệu training AI.

## Daily Pack 01 — 2026-08-30

20 nguồn/bộ tài liệu ưu tiên. Với nguồn không cho phép tái phân phối, chỉ lưu metadata + URL.

| # | Title | Topic / language | Source | License / usage | Description |
|---|---|---|---|---|---|
| 1 | Project CodeNet | Competitive programming / 55+ languages | IBM Research | Kiểm tra LICENSE và điều kiện dataset trước khi tái sử dụng | Kho lớn gồm bài toán lập trình và submissions, hữu ích cho problem solving và code understanding. |
| 2 | AtCoder Datasets | Algorithms / 112 languages | AtCoder | First-party AI-training license; license theo gói | Problems, tests, editorials, reference solutions và verified human solutions. |
| 3 | AtCoder official contests | Algorithms / C++/Python/Java/... | AtCoder | Link/source; tuân thủ terms | Nguồn bài thi chính thức để tạo benchmark và bài tập. |
| 4 | Exercism | Multi-language exercises | Exercism | Kiểm tra license từng phần | Bài tập thực hành theo track, có mentoring và test-driven exercises. |
| 5 | The Algorithms | Algorithms / multi-language | The Algorithms | MIT ở các repo tương ứng; kiểm tra repo cụ thể | Implementations và giải thích thuật toán phục vụ học tập. |
| 6 | The Algorithms C++ | C++ / algorithms | TheAlgorithms/C-Plus-Plus | MIT | Các triển khai thuật toán C++ kèm tài liệu học. |
| 7 | MDN Web Docs | HTML/CSS/JS/Web APIs | Mozilla | Docs CC BY-SA; code samples mới CC0 | Tài liệu web chuẩn, ví dụ code và hướng dẫn API. |
| 8 | The Odin Project | Web development | The Odin Project | Open-source; kiểm tra license từng nội dung | Curriculum web development theo project, từ nền tảng đến full-stack. |
| 9 | Microsoft Python Programming Puzzles | Python / reasoning | Microsoft | Kiểm tra LICENSE của repository trước khi phân phối | Các puzzle Python phục vụ nghiên cứu programming và AI. |
| 10 | SWE-bench | Software engineering / Python | Princeton NLP | Kiểm tra dataset/repository license và điều kiện của underlying repos | Issue thực tế yêu cầu hiểu codebase, sửa lỗi và vượt test suite. |
| 11 | SWE-bench Verified | Software engineering / Python | SWE-bench | Kiểm tra license/terms của dataset và underlying repos | 500 task instances đã được xác minh về khả năng giải. |
| 12 | SWE-smith | SWE-agent training/evaluation | SWE-bench | MIT theo repository | 52K task instances và trajectories dành cho software-engineering agents. |
| 13 | SWE-bench Docker images | Reproducible SWE evaluation | Epoch AI | MIT | Images môi trường đánh giá SWE-bench, hữu ích để tái lập test environments. |
| 14 | SWE-Gym / SWE-Bench Package | Software engineering | SWE-Gym | MIT theo repository | Package và môi trường hỗ trợ benchmark/tasks cho SWE agents. |
| 15 | Project CodeNet problem statements | Problem solving | IBM Research | Kiểm tra license của từng asset | Tách problem statements làm dữ liệu instruction/problem-solving khi được phép. |
| 16 | Project CodeNet submissions | Code generation / repair | IBM Research | Kiểm tra license và provenance | Submissions đa ngôn ngữ, hữu ích cho code understanding và repair. |
| 17 | AtCoder reference solutions | Algorithms / multi-language | AtCoder | Licensed AI-training dataset; tuân thủ gói đã cấp phép | Reference solutions gắn với problem statements và test data. |
| 18 | AtCoder accepted solutions | Code generation / algorithms | AtCoder | Chỉ dùng theo license AI-training tương ứng | Verified human solutions, đa ngôn ngữ và có provenance. |
| 19 | The Algorithms website | Algorithms / CS | The Algorithms | Website MIT; code/explanations theo repo tương ứng | Chỉ mục trực quan của thư viện thuật toán open-source. |
| 20 | SWE-bench evaluation harness | Testing / software engineering | SWE-bench | Kiểm tra repository LICENSE | Harness Docker giúp chạy test và đánh giá patch trên các task SWE. |

## Verified notes for Pack 01

- AtCoder hiện công bố 900+ contests, 5.000+ problems và 30M+ accepted solutions trong bộ dữ liệu được cấp phép riêng cho AI training. Không coi các số liệu này là quyền tự do tái phân phối: phải tuân thủ gói/license đã cấp. 
- MDN xác nhận documentation mặc định theo CC BY-SA 2.5 hoặc mới hơn; code samples thêm từ 20/08/2010 là CC0. Cần attribution đúng với phần documentation được tái sử dụng.
- The Algorithms website ghi website MIT, nhưng license của code/explanations cần kiểm tra ở repository cụ thể.
- SWE-smith công bố 52K task instances và 26K SWE-agent trajectories; repository công bố MIT.

## Evidence links

- AtCoder Datasets: https://datasets.atcoder.jp/
- MDN copyright/licensing: https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Attrib_copyright_license
- The Algorithms website: https://github.com/TheAlgorithms/website
- The Algorithms C++: https://github.com/TheAlgorithms/C-Plus-Plus-1
- SWE-bench: https://github.com/princeton-nlp/SWE-bench
- SWE-smith: https://github.com/SWE-bench/SWE-smith
- SWE-Gym package: https://github.com/SWE-Gym/SWE-Bench-Package

## Corpus accounting

- Daily pack: **20 items**
- Delivered distinct source/resource records: **20**
- Target: **10,000 distinct records**
- Remaining target: **9,980**
- Deduplication key: canonical source URL + dataset/item ID/title
- Copyright rule: do not copy or redistribute protected course/book/repository content unless the applicable license/terms explicitly permit it.
