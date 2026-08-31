# Tài liệu học Trading và Algorithmic Trading

> Bộ tài liệu theo hướng **market fundamentals → technical/fundamental analysis → risk management → quantitative research → backtesting → paper trading**. Nội dung dùng cho học tập, không phải khuyến nghị mua/bán tài sản.

## 1. Nền tảng thị trường

### CME Group — Introduction to Futures
Khóa nhập môn giải thích futures contracts, contract specifications, trading codes, expiration/settlement, tick movements, price limits, notional value, margin và vai trò của speculators/hedgers.

- Nguồn: https://www.cmegroup.com/education/courses/introduction-to-futures

### CME Group — Education Course Catalog
CME Institute có các khóa về futures, options, market fundamentals, strategies/techniques và tools/analytics. Đây là nguồn tốt để học cấu trúc sản phẩm phái sinh từ chính sàn giao dịch.

- Nguồn: https://www.cmegroup.com/education/courses

## 2. Technical Analysis

### CME Group — Technical Analysis
Khóa học bắt đầu từ cách đọc price chart rồi đi vào trend/reversal patterns, support/resistance và oscillators. Tài liệu cũng nhấn mạnh technical analysis dựa trên giả định rằng biến động giá trong quá khứ có thể cung cấp thông tin cho việc đánh giá hướng giá tương lai.

- Nguồn: https://www.cmegroup.com/education/courses/technical-analysis
- Trading and Analysis: https://www.cmegroup.com/education/courses/trading-and-analysis

### Checklist technical analysis
- OHLC và candlestick.
- Trend và market regime.
- Support/resistance.
- Moving averages.
- Momentum/oscillators.
- Volatility.
- Breakout và mean reversion.
- Volume/liquidity khi dữ liệu cho phép.

**Lưu ý:** indicator không tự động tạo ra edge. Cần xác định hypothesis, dữ liệu, execution assumptions và kiểm định out-of-sample.

## 3. Fundamental Analysis

### CME Group — Using Fundamental Analysis When Evaluating Trades
Fundamental analysis của futures tập trung vào việc ước lượng model price hiện tại/tương lai dựa trên economic data, industry conditions và supply/demand. Nội dung thay đổi theo từng loại sản phẩm.

- Nguồn: https://www.cmegroup.com/education/courses/using-fundamental-analysis-when-evaluating-trades

### Cách học
1. Xác định asset và economic drivers.
2. Phân biệt leading/coincident/lagging indicators.
3. Theo dõi supply/demand.
4. Ghi lại hypothesis trước khi xem kết quả.
5. Đánh giá sensitivity của giá với từng biến.

## 4. Risk Management

### FINRA — Day Trading
FINRA định nghĩa day trading là mua/bán cùng một security trong cùng ngày trong margin account nhằm kiếm lợi từ biến động giá nhỏ. Tài liệu cảnh báo day trading đòi hỏi hiểu thị trường, hệ thống thực hiện lệnh và rủi ro margin; FINRA cũng lưu ý day trading nhìn chung không phù hợp với người có nguồn lực hạn chế, ít kinh nghiệm hoặc mức chịu rủi ro thấp.

- Nguồn: https://www.finra.org/investors/investing/investment-products/stocks/day-trading
- Margin accounts: https://www.finra.org/rules-guidance/key-topics/margin-accounts

### Risk checklist
- Position sizing.
- Maximum loss per trade.
- Maximum daily/weekly drawdown.
- Stop-loss logic và failure modes.
- Leverage/margin.
- Liquidity và slippage.
- Transaction fees.
- Gap risk.
- Correlation và portfolio concentration.
- Kill switch cho algorithm.

Không dùng tiền vay, tiền sinh hoạt hoặc quỹ khẩn cấp cho hoạt động đầu cơ rủi ro cao.

## 5. Quantitative Trading

### QuantConnect — Writing Algorithms
Tài liệu hướng dẫn xây algorithmic trading strategy với concepts như securities, portfolio, universe selection, datasets, historical data, orders và reality modeling cho fills, slippage và fees.

- Nguồn: https://www.quantconnect.com/docs/v2/writing-algorithms

### Kiến trúc một strategy
```text
Market data
    ↓
Data cleaning / normalization
    ↓
Feature / indicator calculation
    ↓
Signal generation
    ↓
Portfolio / position sizing
    ↓
Risk controls
    ↓
Order generation
    ↓
Execution model
    ↓
Logging + metrics
```

## 6. Backtesting

### QuantConnect — Backtesting
Backtesting là mô phỏng algorithm trên historical data để đánh giá cách strategy từng hoạt động trong quá khứ. Tài liệu cũng nhấn mạnh rằng past performance không bảo đảm future performance.

- Getting started: https://www.quantconnect.com/docs/v2/cloud-platform/backtesting/getting-started
- Results: https://www.quantconnect.com/docs/v2/cloud-platform/backtesting/results

### Các bước backtest đúng
1. Viết hypothesis trước khi nhìn kết quả.
2. Xác định universe và data frequency.
3. Tách in-sample/out-of-sample.
4. Mô hình hóa fee, spread, slippage và latency phù hợp.
5. Kiểm tra look-ahead bias.
6. Kiểm tra survivorship bias.
7. Chạy sensitivity/parameter analysis.
8. Walk-forward hoặc rolling validation khi phù hợp.
9. Ghi lại mọi thay đổi strategy.
10. Chỉ sau khi vượt các kiểm định mới chuyển sang paper trading.

## 7. Hypothesis-driven research và overfitting

### QuantConnect — Research Guide
Research nên bắt đầu bằng một central hypothesis; quá trình nghiên cứu dùng dữ liệu để kiểm tra hypothesis thay vì liên tục thay hypothesis theo backtest tốt nhất. Tài liệu có các chủ đề parameter detection, overfitting và out-of-sample period.

- Nguồn: https://www.quantconnect.com/docs/v2/cloud-platform/backtesting/research-guide

### Cần đặc biệt tránh
- Chọn strategy vì backtest đẹp rồi mới tìm câu chuyện giải thích.
- Tối ưu quá nhiều parameters.
- Data snooping.
- Look-ahead bias.
- Leakage từ future information.
- Dùng closing price mà không mô hình hóa khả năng thực thi tại close.
- Bỏ qua fee/slippage.
- Chỉ báo cáo CAGR mà bỏ qua drawdown, volatility và tail risk.

## 8. Backtest → Paper Trading → Live

QuantConnect hỗ trợ quy trình từ research/backtest tới paper trading và live algorithm. Tài liệu live trading cũng lưu ý rằng kết quả live thường khác backtest vì data, modeling, brokerage và real-time execution có thể khác mô phỏng.

- Getting started: https://www.quantconnect.com/docs/v2/cloud-platform/getting-started
- Live trading: https://www.quantconnect.com/docs/v2/writing-algorithms/live-trading
- Reconciliation: https://www.quantconnect.com/docs/v2/writing-algorithms/live-trading/reconciliation

### Gate đề xuất
```text
Hypothesis
  ↓
Historical data validation
  ↓
Backtest
  ↓
Out-of-sample validation
  ↓
Robustness / sensitivity tests
  ↓
Paper trading
  ↓
Execution reconciliation
  ↓
Small-scale live deployment (nếu phù hợp)
```

## 9. Dùng Python cho trading research

Kết hợp tài liệu coding với trading:

### NumPy
Dùng cho vectorized numerical computation, arrays, statistics và các phép toán ma trận.
- https://numpy.org/doc/stable/user/

### pandas
Dùng để xử lý OHLCV/time-series: timestamp alignment, resampling, rolling windows, joins, missing data, groupby và feature engineering.
- https://pandas.pydata.org/docs/getting_started/

### scikit-learn
Dùng khi nghiên cứu ML-based signals sau khi đã hiểu data leakage, cross-validation và out-of-sample evaluation.
- https://scikit-learn.org/stable/user_guide.html

## 10. Bộ chỉ số cần theo dõi

### Return
- Total return.
- CAGR.
- Benchmark-relative return.

### Risk
- Volatility.
- Maximum drawdown.
- Drawdown duration.
- Value at Risk / Expected Shortfall khi mô hình phù hợp.

### Risk-adjusted performance
- Sharpe ratio.
- Sortino ratio.
- Calmar ratio.

### Trading quality
- Win rate.
- Average win/loss.
- Profit factor.
- Expectancy.
- Turnover.
- Average holding period.
- Fees/slippage as % of gross PnL.

Không đánh giá strategy bằng một metric duy nhất.

## 11. Project luyện tập

### Project 1 — Rule-based backtest
- Chọn một liquid asset.
- Tạo strategy trend-following đơn giản.
- Dùng fixed position sizing.
- Thêm fees/slippage.
- Report return, drawdown, Sharpe và trade statistics.

### Project 2 — Mean reversion
- Xây signal dựa trên rolling statistics.
- Kiểm tra behavior trong nhiều market regimes.
- So sánh in-sample và out-of-sample.

### Project 3 — ML signal research
- Tạo feature từ historical data.
- Split theo thời gian, không random shuffle nếu gây leakage.
- Train model.
- Đánh giá prediction và trading performance tách biệt.
- Chạy walk-forward/out-of-sample.

### Project 4 — Paper trading system
- Data feed.
- Signal engine.
- Risk engine.
- Order manager.
- Position reconciliation.
- Logging.
- Alert/kill switch.

## 12. Quy tắc nghiên cứu trading

1. **Hypothesis trước, backtest sau.**
2. Không dùng future information.
3. Luôn mô hình hóa chi phí giao dịch khi có thể.
4. Tách in-sample và out-of-sample.
5. Kiểm tra robustness thay vì chọn parameter tối ưu nhất.
6. So sánh với baseline/benchmark.
7. Theo dõi drawdown và tail risk, không chỉ lợi nhuận.
8. Paper trade trước khi cân nhắc live deployment.
9. Khi live, so sánh execution thực tế với backtest và điều tra sai lệch.
10. Không xem backtest là bằng chứng strategy sẽ sinh lời trong tương lai.

## 13. Nguồn tham khảo chính

| Chủ đề | Nguồn | Mục đích |
|---|---|---|
| Futures | CME Introduction to Futures | Cấu trúc futures, margin, tick, settlement |
| Technical analysis | CME Technical Analysis | Chart, trend, support/resistance, indicators |
| Fundamental analysis | CME Fundamental Analysis | Supply/demand và economic drivers |
| Risk | FINRA Day Trading | Rủi ro day trading và margin |
| Algorithmic trading | QuantConnect Writing Algorithms | Xây strategy và execution model |
| Backtesting | QuantConnect Backtesting | Historical simulation + metrics |
| Research | QuantConnect Research Guide | Hypothesis, overfitting, OOS |
| Live trading | QuantConnect Live Trading | Paper/live deployment và reconciliation |
| Data | NumPy + pandas | Quant research data pipeline |
| ML | scikit-learn | Modeling và evaluation |

## 14. Bản quyền và sử dụng

File này là bản **tổng hợp và ghi chú**, không sao chép toàn văn tài liệu nguồn. Khi xây corpus/training data, cần kiểm tra license, terms, provenance và quyền tái phân phối của từng dataset/tài liệu. Với nguồn không cho phép tái phân phối, chỉ lưu metadata, mô tả và URL nguồn.

## 15. Disclaimer

Trading và algorithmic trading có rủi ro mất vốn. Nội dung này phục vụ học tập và nghiên cứu kỹ thuật; không phải tư vấn đầu tư, không đảm bảo lợi nhuận và không thay thế quy định pháp lý, tài liệu của broker/exchange hoặc tư vấn chuyên môn.
