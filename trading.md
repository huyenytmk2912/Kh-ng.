# Tài liệu học Trading và Algorithmic Trading

> Bộ tài liệu theo hướng **market fundamentals → technical/fundamental analysis → risk management → quantitative research → backtesting → paper trading**. Nội dung phục vụ học tập/nghiên cứu, không phải khuyến nghị mua bán.

## 1. Nền tảng thị trường

### CME Group — Introduction to Futures
Khóa nhập môn giải thích futures contracts, contract specifications, trading codes, expiration/settlement, tick movements, price limits, notional value, margin và vai trò của speculators/hedgers. Đây là điểm bắt đầu tốt nếu muốn hiểu cơ chế của phái sinh trước khi code strategy.

- Nguồn: https://www.cmegroup.com/education/courses/introduction-to-futures

### CME Institute Education
CME cung cấp khóa học và công cụ thực hành về futures/options, market fundamentals, strategies và analytics; trang Education cũng có Trading Simulator để luyện mà không dùng tiền thật.

- Nguồn: https://www.cmegroup.com/education

## 2. Technical Analysis

Học chart và indicator như công cụ tạo hypothesis, không coi indicator là bằng chứng về edge.

### Nội dung cần nắm
- OHLC và candlestick.
- Trend và market regime.
- Support/resistance.
- Moving averages.
- Momentum/oscillators.
- Volatility.
- Breakout và mean reversion.
- Volume/liquidity khi dữ liệu cho phép.

**Workflow:** hypothesis → historical data → backtest → out-of-sample → robustness. Không chọn strategy chỉ vì một biểu đồ/backtest đẹp.

- CME Education: https://www.cmegroup.com/education

## 3. Fundamental Analysis

Fundamental research cần liên kết giá với economic drivers, supply/demand, industry conditions và các biến có thể quan sát. Với futures, driver thay đổi theo sản phẩm; cần xác định thesis trước khi xem kết quả.

### Quy trình
1. Xác định asset và economic drivers.
2. Phân biệt leading/coincident/lagging indicators.
3. Theo dõi supply/demand.
4. Ghi hypothesis trước khi xem PnL.
5. Đánh giá sensitivity của giá với từng biến.
6. Kiểm tra thesis trong nhiều market regimes.

## 4. Risk Management

### CME — Trade and Risk Management
CME nhấn mạnh risk management bắt đầu từ từng giao dịch: biết điểm thoát, quy mô tài khoản và lượng vốn có thể chịu rủi ro. Quản trị rủi ro bao gồm lựa chọn thị trường, allocation, position size và kiểm soát overtrading.

- Nguồn: https://www.cmegroup.com/education/courses/trade-and-risk-management

### SEC — Day Trading: Your Dollars at Risk
SEC cảnh báo day trading có thể gây tổn thất lớn, đặc biệt khi dùng borrowed money/leverage. Đây là tài liệu cần đọc trước khi nghiên cứu hệ thống day trading.

- Nguồn: https://www.sec.gov/about/reports-publications/investorpubsdaytipshtm

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

Không dùng tiền sinh hoạt hoặc quỹ khẩn cấp cho hoạt động đầu cơ rủi ro cao.

## 5. Futures và Micro Futures

CME có tài liệu riêng về micro futures. Các hợp đồng micro có quy mô nhỏ hơn hợp đồng tương ứng, giúp điều chỉnh exposure và risk granularity tốt hơn; vẫn phải hiểu margin, tick value, liquidity và contract specifications.

- Introduction to Futures: https://www.cmegroup.com/education/courses/introduction-to-futures
- Micro Futures: https://www.cmegroup.com/education/courses/understanding-micro-futures-contracts-at-cme-group
- Futures Spreads: https://www.cmegroup.com/education/courses/understanding-futures-spreads

## 6. Quantitative Trading

### QuantConnect — Research Engine
Research Environment dựa trên Jupyter, hỗ trợ Python/C# và `QuantBook`. QuantConnect khuyến nghị kiểm tra hypothesis trong Research Environment trước khi backtest; môi trường research cũng phù hợp để train/inspect ML models trước khi đưa vào backtest/live.

- Nguồn: https://www.quantconnect.com/docs/v2/research-environment/key-concepts/research-engine

### Kiến trúc strategy
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

## 7. Backtesting

Backtest là mô phỏng strategy trên historical data, không phải bằng chứng strategy sẽ có lợi nhuận trong tương lai.

### Quy trình kiểm định
1. Viết hypothesis trước khi xem kết quả.
2. Xác định universe và data frequency.
3. Tách in-sample/out-of-sample.
4. Mô hình hóa fee, spread, slippage và latency phù hợp.
5. Kiểm tra look-ahead bias.
6. Kiểm tra survivorship bias.
7. Kiểm tra data leakage.
8. Chạy sensitivity/parameter analysis.
9. Walk-forward/rolling validation khi phù hợp.
10. Ghi lại mọi thay đổi strategy.
11. Chỉ sau robustness testing mới chuyển sang paper trading.

- QuantConnect Backtesting: https://www.quantconnect.com/docs/v2/cloud-platform/backtesting/getting-started
- Results: https://www.quantconnect.com/docs/v2/cloud-platform/backtesting/results

## 8. Hypothesis-driven research và overfitting

Research tốt bắt đầu bằng câu hỏi có thể kiểm chứng. Không nên chạy hàng trăm biến thể rồi chọn kết quả tốt nhất và sau đó mới tạo câu chuyện giải thích.

### Cần tránh
- Data snooping.
- Look-ahead bias.
- Future-information leakage.
- Survivorship bias.
- Quá nhiều parameters so với lượng dữ liệu.
- Tối ưu theo một giai đoạn thị trường duy nhất.
- Dùng closing price nhưng giả định execution tại close không thực tế.
- Bỏ qua fee/slippage.
- Chỉ báo cáo CAGR mà bỏ qua drawdown, volatility và tail risk.

**Nguyên tắc:** một strategy tốt cần evidence về robustness, không chỉ một equity curve đẹp.

- QuantConnect Research/Backtesting docs: https://www.quantconnect.com/docs/v2/research-environment/key-concepts/research-engine

## 9. Python cho trading research

### NumPy
Dùng cho vectorized numerical computation, arrays, statistics, linear algebra và simulation.
- https://numpy.org/doc/stable/user/

### pandas
Dùng cho OHLCV/time-series: timestamp alignment, resampling, rolling windows, joins, missing data, groupby và feature engineering.
- https://pandas.pydata.org/docs/user_guide/

### scikit-learn
Dùng cho ML signals sau khi hiểu temporal validation, leakage, preprocessing pipelines và out-of-sample evaluation.
- https://scikit-learn.org/stable/user_guide.html

### Data pipeline mẫu
```text
Raw OHLCV/news/fundamental data
        ↓
Schema + timestamp validation
        ↓
Cleaning / corporate-action handling
        ↓
Feature engineering
        ↓
Time-aware train/validation split
        ↓
Model / signal
        ↓
Backtest with costs
        ↓
OOS / walk-forward
```

## 10. Metrics cần theo dõi

### Return
- Total return.
- CAGR.
- Benchmark-relative return.

### Risk
- Volatility.
- Maximum drawdown.
- Drawdown duration.
- VaR / Expected Shortfall khi mô hình phù hợp.

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

## 11. Backtest → Paper Trading → Live

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

Live trading có thể khác backtest do data, fills, slippage, fees, brokerage và latency. Vì vậy cần reconciliation giữa expected order/position và execution thực tế.

## 12. Project luyện tập

### Project 1 — Rule-based backtest
- Chọn một liquid asset.
- Strategy trend-following đơn giản.
- Fixed position sizing.
- Thêm fees/slippage.
- Report return, drawdown, Sharpe và trade statistics.

### Project 2 — Mean reversion
- Signal dựa trên rolling statistics.
- Kiểm tra nhiều market regimes.
- So sánh in-sample và out-of-sample.

### Project 3 — ML signal research
- Feature từ historical data.
- Split theo thời gian; không random shuffle nếu gây leakage.
- Train model.
- Đánh giá prediction và trading performance tách biệt.
- Walk-forward/out-of-sample.

### Project 4 — Paper trading system
- Data feed.
- Signal engine.
- Risk engine.
- Order manager.
- Position reconciliation.
- Logging.
- Alert/kill switch.

## 13. Quy tắc nghiên cứu trading

1. **Hypothesis trước, backtest sau.**
2. Không dùng future information.
3. Mô hình hóa transaction costs khi có thể.
4. Tách in-sample và out-of-sample.
5. Kiểm tra robustness thay vì chọn parameter tối ưu nhất.
6. So sánh với baseline/benchmark.
7. Theo dõi drawdown và tail risk, không chỉ lợi nhuận.
8. Paper trade trước khi cân nhắc live deployment.
9. Khi live, reconciliation execution với backtest assumptions.
10. Không xem backtest là bảo đảm lợi nhuận tương lai.

## 14. Nguồn tham khảo chính

| Chủ đề | Nguồn | Mục đích |
|---|---|---|
| Futures | CME Introduction to Futures | Contract, margin, tick, settlement |
| Risk | CME Trade and Risk Management | Position sizing và risk control |
| Day trading risk | SEC | Rủi ro và leverage |
| Futures practice | CME Education | Courses + simulator |
| Quant research | QuantConnect Research Engine | Hypothesis/data research |
| Backtesting | QuantConnect | Historical simulation + metrics |
| Numerical data | NumPy | Vectorized computing |
| Time series | pandas | DataFrame/time series |
| ML | scikit-learn | Modeling/evaluation |

## 15. Bản quyền và sử dụng

File này là **bản tổng hợp và ghi chú**, không sao chép toàn văn tài liệu nguồn. Khi xây corpus/training data, cần kiểm tra license, terms, provenance và quyền tái phân phối của từng dataset/tài liệu. Với nguồn không cho phép tái phân phối, chỉ lưu metadata, mô tả và URL.

## 16. Disclaimer

Trading và algorithmic trading có rủi ro mất vốn. Nội dung này phục vụ học tập và nghiên cứu kỹ thuật; không phải tư vấn đầu tư, không đảm bảo lợi nhuận và không thay thế quy định pháp lý, tài liệu của broker/exchange hoặc tư vấn chuyên môn.
