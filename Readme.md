# The Trading Risk Profiler Project

## Introduction
Welcome to the Trading Risk Profiler, a tool designed to align algorithmic trading strategies with personal risk tolerance. Utilizing a chatbot, it assesses financial objectives and risk preferences to suggest suitable trading strategies.

## Key Features
- **Chatbot for Risk Assessment**: Interactive tool to determine your risk level.
- **Three Core Trading Strategies**: Recommendations based on risk profile, including Bollinger Bands, RSI Crossover, and Price SMA Crossover.
- **Sharpe Ratio Analysis**: Backtesting strategies to find Sharpe Ratios correlating with risk levels.
- **Cryptocurrency Trading**: Focus on crypto to avoid equity market limitations.
- **Quantconnect for Paper Trading and Backtesting**: Utilize Quantconnect for simulation purposes.
- **Backtest.py Utility**: Custom script for strategy evaluation.
- **Pytorch Machine Learning**: Incorporating advanced predictive modeling.

## Trading Strategies Explained
- **Bollinger Bands and RSI Combined**: Identifies overbought and oversold regions for buy/sell decisions.
- *This strategy combines Bollinger Bands and RSI to identify potential buy and sell points based on perceived oversold and overbought conditions, respectively. It assumes that an asset's price will revert back towards a mean or average level after reaching extreme high or low valuations. This approach is common in range-bound or sideways markets, where the asset price oscillates within a certain range.
-## Backtest with Bollinger Bands
- ## Strategy Analysis Summary

# #Market Activity
- **Active Time in Market:** 89.38%, indicating frequent trading or extended position holding.

## Equity Performance
- **Final Equity Value:** $95,519.99 (down from a peak of $158,358.98).
- **Overall Return:** -4.48% (net loss over the period).
- **Annualized Return:** -4.24%, with an annualized volatility of 43.40%.

## Comparison with Buy & Hold
- **Buy-and-Hold Return:** 104.33%, significantly outperforming the trading strategy.

## Risk-Adjusted Return Metrics
- **Sharpe, Sortino, and Calmar Ratios:** All 0.0, indicating no excess return for the level of risk.

## Drawdowns
- **Maximum Drawdown:** -42.90% (largest drop in portfolio value).
- **Average Drawdowns:** -5.88%, lasting 16 days on average, with the longest being 101 days.

## Trading Performance
- **Total Trades:** 36 with a 33.33% win rate.
- **Best Trade:** +25.50% return.
- **Worst Trade:** -17.59% loss.
- **Average Trade Return:** -0.13%.

## Trade Durations
- **Longest Trade:** 42 days.
- **Average Trade Duration:** 10 days.

## Profitability Metrics
- **Profit Factor:** 1.07 (marginal profitability).
- **Expectancy:** 0.17% (average amount earned per trade).
- **System Quality Number (SQN):** -0.08, indicating poor system performance.
  
## Summary
- The strategy underperformed compared to a simple buy-and-hold approach, resulting in a net loss.
- High volatility and significant drawdowns suggest high risk.
- Zero values in risk-adjusted metrics (Sharpe, Sortino, Calmar) show insufficient returns for the risks taken.
- Despite numerous trades, overall effectiveness is limited, with negative returns and a low win rate.
- The analysis suggests a need for strategy revision, including better risk management, refined trading algorithms, and improved market alignment.

- **Price SMA Crossover**: Employs Simple Moving Averages; buy signals when short-term SMA crosses above long-term SMA.

## Conclusion
The Trading Risk Profiler is tailored for both beginners and experienced traders, aiming to make algorithmic trading more accessible by aligning strategies with individual risk profiles.

---

Your feedback and contributions to this project are welcome and appreciated!


