# Tài liệu học Trading + Algorithmic Trading

> Curriculum: market fundamentals → technical/fundamental research → risk management → quantitative research → backtesting → paper trading. Nội dung phục vụ học tập/nghiên cứu, không phải khuyến nghị mua bán.

## 1. Futures fundamentals — CME

CME Introduction to Futures giải thích futures contracts, contract specifications, trading codes, expiration/settlement, tick movements, price limits, notional value, margin và vai trò của hedgers/speculators.

**Cần hiểu trước khi code:** contract size, tick value, notional exposure, initial/maintenance margin, expiry/roll, settlement và liquidity.

Nguồn: https://www.cmegroup.com/education/courses/introduction-to-futures
CME Education: https://www.cmegroup.com/education

## 2. Technical analysis như hypothesis generator

Technical analysis nên dùng để tạo hypothesis, không phải bằng chứng rằng strategy có edge.

Nội dung: OHLC/candlestick, trend, market regime, support/resistance, moving averages, momentum, volatility, breakout, mean reversion và volume/liquidity.

Workflow:

```text
hypothesis → historical data → backtest → OOS → robustness → paper trading
```

Không chọn strategy chỉ vì equity curve đẹp.

## 3. Fundamental / macro research

Với mỗi asset, xác định economic drivers trước khi xem PnL: supply/demand, rates, inflation, growth, inventories, seasonality, industry conditions hoặc các biến đặc thù sản phẩm.

Quy trình:
1. Xác định asset và driver.
2. Phân loại leading/coincident/lagging indicators.
3. Viết thesis trước khi xem kết quả.
4. Xác định biến nào có thể quan sát tại thời điểm ra quyết định.
5. Kiểm tra thesis trên nhiều market regimes.

## 4. Risk management

CME nhấn mạnh risk management bắt đầu từ việc biết thị trường, allocation, position size và điểm exit. Trước mỗi trade cần biết mức vốn có thể chịu rủi ro.

Nguồn: https://www.cmegroup.com/education/courses/trade-and-risk-management

### Risk checklist
- Position sizing.
- Maximum loss/trade.
- Maximum daily/weekly drawdown.
- Stop-loss logic và failure modes.
- Leverage/margin.
- Liquidity và slippage.
- Transaction fees.
- Gap/tail risk.
- Correlation/concentration.
- Algorithm kill switch.

Không dùng tiền sinh hoạt/quỹ khẩn cấp cho hoạt động đầu cơ rủi ro cao.

## 5. Micro Futures và Futures Spreads

Micro futures có quy mô hợp đồng nhỏ hơn sản phẩm tương ứng, giúp điều chỉnh exposure và risk granularity; vẫn phải hiểu tick value, margin, liquidity và contract specification.

Nguồn:
- https://www.cmegroup.com/education/courses/understanding-micro-futures-contracts-at-cme-group
- https://www.cmegroup.com/education/courses/understanding-futures-spreads

## 6. Quantitative research với Python

### NumPy
Arrays, vectorized computation, statistics, linear algebra và simulation.
https://numpy.org/doc/stable/user/

### pandas
OHLCV/time-series, timestamp alignment, resampling, rolling windows, joins, missing data và feature engineering.
https://pandas.pydata.org/docs/user_guide/

### scikit-learn
ML signals chỉ nên dùng sau khi hiểu temporal validation, leakage, preprocessing pipelines và OOS evaluation.
https://scikit-learn.org/stable/user_guide.html

### Data pipeline

```text
raw OHLCV/news/fundamental
        ↓
schema + timestamp validation
        ↓
cleaning / normalization
        ↓
feature engineering
        ↓
time-aware split
        ↓
model / signal
        ↓
backtest + costs
        ↓
OOS / walk-forward
```

## 7. QuantConnect Research Environment

QuantConnect Research là môi trường Jupyter dùng `QuantBook`, hỗ trợ Python/C#. Tài liệu khuyến nghị kiểm tra hypothesis trong Research Environment trước khi backtest; ML model cũng có thể train/inspect ở research rồi đưa vào backtest/live.

Nguồn: https://www.quantconnect.com/docs/v2/research-environment
Research getting started: https://www.quantconnect.com/docs/v2/cloud-platform/research/getting-started

Kiến trúc strategy nên tách:

```text
Market data
  ↓
Data cleaning
  ↓
Features / indicators
  ↓
Signal
  ↓
Portfolio / sizing
  ↓
Risk controls
  ↓
Order generation
  ↓
Execution
  ↓
Logging + metrics
```

## 8. Backtesting

Backtest là mô phỏng historical, không phải bảo đảm lợi nhuận tương lai.

### Quy trình kiểm định
1. Viết hypothesis trước khi xem kết quả.
2. Xác định universe và data frequency.
3. Tách in-sample/out-of-sample.
4. Mô hình hóa fee, spread, slippage và latency.
5. Kiểm tra look-ahead bias.
6. Kiểm tra survivorship bias.
7. Kiểm tra data leakage.
8. Sensitivity/parameter analysis.
9. Walk-forward/rolling validation.
10. Ghi toàn bộ experiment history.

QuantConnect backtesting docs: https://www.quantconnect.com/docs/v2/cloud-platform/backtesting/getting-started

Tài liệu hiện tại còn hỗ trợ đặt OOS holdout period để giảm nguy cơ overfitting trong quá trình research.

## 9. Backtest analysis / meta-analysis

Không chỉ nhìn CAGR. Có thể load backtest results vào Research Environment để phân tích fills, churn, statistics và so sánh nhiều backtest.

Nguồn: https://www.quantconnect.com/docs/v2/research-environment/meta-analysis/backtest-analysis

Câu hỏi cần trả lời:
- Lợi nhuận đến từ giai đoạn nào?
- Strategy có phụ thuộc một vài trade lớn không?
- Turnover/churn có ăn mòn PnL không?
- Kết quả có tương quan cao với strategy khác không?
- Performance có giữ được ngoài sample không?

## 10. Overfitting và research hygiene

Tránh:
- Data snooping.
- Look-ahead bias.
- Future-information leakage.
- Survivorship bias.
- Quá nhiều parameters.
- Tối ưu trên một regime duy nhất.
- Execution giả định không thực tế.
- Bỏ qua fee/slippage.
- Chỉ báo cáo CAGR.

**Nguyên tắc:** strategy cần evidence về robustness, không chỉ một backtest tốt nhất.

## 11. Metrics

### Return
Total return, CAGR, benchmark-relative return.

### Risk
Volatility, maximum drawdown, drawdown duration, VaR/Expected Shortfall khi phù hợp.

### Risk-adjusted
Sharpe, Sortino, Calmar.

### Trading quality
Win rate, average win/loss, profit factor, expectancy, turnover, holding period, fees/slippage as % gross PnL.

Không đánh giá strategy bằng một metric duy nhất.

## 12. Backtest → Paper → Live

QuantConnect có workflow từ project → backtest → paper trading → live deployment. Paper trading là bước kiểm tra data feed, fills, latency, reconciliation và operational behavior trước live.

Nguồn: https://www.quantconnect.com/docs/v2/cloud-platform/getting-started

```text
Hypothesis
  ↓
Data validation
  ↓
Backtest
  ↓
OOS / walk-forward
  ↓
Robustness
  ↓
Paper trading
  ↓
Execution reconciliation
  ↓
Small-scale live (nếu phù hợp)
```

## 13. AI coding agents cho trading research

AI coding agents có thể tăng tốc data engineering, research tooling, backtest harness và test generation. Không nên giao cho agent quyền tự quyết định trade hoặc bỏ qua validation.

Workflow:

```text
Trading hypothesis
      ↓
Human-defined assumptions
      ↓
AI-assisted implementation
      ↓
Unit tests + data validation
      ↓
Backtest + fees/slippage
      ↓
OOS / walk-forward
      ↓
Paper trading
      ↓
Human approval
```

### Agent được phép
- Viết feature engineering code.
- Viết test timestamp alignment.
- Kiểm tra missing/duplicate rows.
- Chạy backtest theo config cố định.
- Tạo metrics report.
- Phân loại lỗi.

### Agent không được phép
- Tự đổi risk limits.
- Tự gửi live orders.
- Đọc API secrets.
- Tự chọn strategy tốt nhất sau hàng trăm thử nghiệm mà không lưu experiment history.

## 14. Experiment tracking

Mỗi experiment phải lưu:

```text
experiment_id
code_commit
config/parameters
data_version
time_range
transaction_cost assumptions
in-sample range
out-of-sample range
metrics
warnings
artifacts
```

Mục tiêu: có thể tái tạo kết quả từ một code commit + data version cụ thể. Đây là biện pháp chống data snooping và hỗ trợ audit.

## 15. Coding agent / context engineering cho quant

### Hugging Face Agents Course
Học agent fundamentals, tools/actions, framework và evaluation; phù hợp để xây research agent có tool giới hạn quyền.
https://huggingface.co/agents-course

### Hugging Face Context Course
Học Skills, MCP, Plugins, Subagents và Hooks. Có thể dùng để tổ chức knowledge/context cho quant repository và kiểm soát agent lifecycle.
https://huggingface.co/context-course
https://huggingface.co/learn/context-course/unit0/introduction

### SWE-bench Verified
Dùng làm tham khảo cho methodology đánh giá coding agent bằng task thực tế và test, thay vì đánh giá bằng subjective code review.
https://www.swebench.com/verified.html

## 16. Projects luyện tập

### Project 1 — Rule-based backtest
Trend-following đơn giản trên liquid asset; fixed sizing; fees/slippage; report return, drawdown, Sharpe, trade statistics.

### Project 2 — Mean reversion
Rolling statistics; nhiều market regimes; so sánh IS/OOS; sensitivity analysis.

### Project 3 — ML signal
Features từ historical data; time-aware split; model; prediction metrics riêng với trading metrics; walk-forward validation.

### Project 4 — Paper trading engine
Data feed → signal → risk → order manager → reconciliation → logging → kill switch.

### Project 5 — AI-assisted quant research
Agent chỉ được đọc dataset, sửa code trong workspace và chạy test/backtest. Mọi experiment phải gắn code commit, data version và config.

## 17. Nguồn cập nhật — 31/08/2026

| Chủ đề | Nguồn | Nội dung |
|---|---|---|
| Futures | CME Introduction to Futures | Contract, margin, tick, settlement |
| Risk | CME Trade and Risk Management | Position sizing, exits, risk control |
| Futures practice | CME Education | Courses và simulator |
| Quant research | QuantConnect Research | Jupyter/QuantBook, data, ML |
| Backtesting | QuantConnect | Historical simulation, OOS, results |
| Backtest analysis | QuantConnect Meta Analysis | Fills, churn, comparison |
| Numerical | NumPy | Vectorized computation |
| Time series | pandas | DataFrame/time-series |
| ML | scikit-learn | Modeling/evaluation |
| AI agents | Hugging Face | Agents/context engineering |

Các trang QuantConnect hiện mô tả Research Environment, backtesting, meta-analysis và paper/live workflow; CME vẫn cung cấp các khóa nền tảng về futures và risk management. citeturn1search0turn1search7turn1search13turn1search11turn1search4turn1search6

## 18. Provenance và disclaimer

File này là bản tổng hợp/ghi chú, không sao chép toàn văn nguồn. Khi xây corpus/training data cần kiểm tra license, terms, provenance và quyền tái phân phối.

Trading và algorithmic trading có rủi ro mất vốn. Nội dung này phục vụ học tập và nghiên cứu kỹ thuật; không phải tư vấn đầu tư, không đảm bảo lợi nhuận và không thay thế quy định của broker/exchange hoặc tư vấn chuyên môn.