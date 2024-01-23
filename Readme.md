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

- # SVM Model Performance Summary

## Training Set Performance
- **Accuracy:** 91% on the training set.
- **Class-wise Performance:**
  - **Class -1.0 (Sell):** Precision 100%, Recall 28%.
  - **Class 0.0 (Hold):** Precision 91%, Recall 100%.
  - **Class 1.0 (Buy):** Precision and Recall 0%.

**Summary:** The model excelled in identifying 'hold' signals but had difficulties with 'buy' and 'sell' signals, particularly failing to detect any 'buy' signals.

## Testing Set Performance
- **Accuracy:** 90% on the testing set.
- **Class-wise Performance:**
  - **Class -1.0 (Sell):** Precision and Recall 0%.
  - **Class 0.0 (Hold):** Precision 90%, Recall 100%.

**Summary:** Consistent with training performance, the model effectively identified 'hold' signals but failed to recognize any 'sell' signals and did not predict 'buy' signals in the test data.

## Overall Summary
The SVM model demonstrated strong performance in accurately recognizing 'hold' signals. However, it significantly underperformed in identifying 'buy' and 'sell' signals. This led to high overall accuracy, primarily attributed to its effectiveness with the 'hold' class, which seems to be more prevalent in the dataset. The model's skewed performance across different classes suggests the need for further tuning or a different approach to enhance its ability to identify 'buy' and 'sell' signals. The results also indicate a potential imbalance in the dataset, which may have influenced the model's learning bias towards the 'hold' signals.

# Optimized SVM Model Performance Summary Using GridSearchCV for hyperparameter tuning

## Introduction
The outcomes discussed are based on an optimized Support Vector Machine (SVM) model, enhanced using GridSearchCV from scikit-learn. This optimization has notably improved the model's ability to identify trading signals compared to the initial SVM model.

## Training Set Performance
- **Overall Accuracy:** Increased to 97%, showing a high rate of correct predictions.
- **Class-wise Performance:**
  - **Class -1.0 (Sell):** Precision 100%, Recall 83% - excellent at identifying sell signals.
  - **Class 0.0 (Hold):** Precision 97%, Recall 100% - highly effective for hold signals.
  - **Class 1.0 (Buy):** Precision 100%, Recall 55% - reliable in buy predictions but misses some buy opportunities.

**Summary:** Post hyperparameter tuning, the model demonstrates a well-balanced and effective performance across all trading signal classes.

## Testing Set Performance
- **Overall Accuracy:** Maintained at 94%, indicating effective generalization to unseen data.
- **Class-wise Performance:**
  - **Class -1.0 (Sell):** Precision 64%, Recall 100% - proficient in identifying most sell opportunities, though with some false positives.
  - **Class 0.0 (Hold):** Maintains perfect precision and high recall.

**Summary:** The model shows strong generalization capabilities, with notable improvement in identifying sell signals compared to the initial version.

## Overall Summary
- **Hyperparameter Tuning Impact:** The use of GridSearchCV has substantially enhanced the SVM model's differentiation between buy, hold, and sell signals.
- **Significant Improvements:** Notably better precision and recall for sell and buy signals, addressing previous weaknesses.
- **Balanced Performance:** The model now excels in recognizing hold signals and effectively identifies buy and sell opportunities.
- **Robust and Reliable:** Improved performance on both training and testing sets indicates a well-tuned model suitable for practical trading applications.
- **Advancement in Trading Strategy:** This optimized model marks a significant step forward, showcasing the importance of thorough hyperparameter tuning in machine learning models for trading.


- **Price SMA Crossover**: Employs Simple Moving Averages; buy signals when short-term SMA crosses above long-term SMA.
# Trading Strategy Performance Recap

## Overview
- **Start Date:** 2016-01-04
- **End Date:** 2024-01-08
- **Duration:** 2926 days

## Market Exposure
- **Exposure Time:** 97.92%

## Equity Performance
- **Final Equity:** $148,395.57
- **Equity Peak:** $177,583.42
- **Return:** 48.40%
- **Buy & Hold Return:** 583.74%
- **Annualized Return:** 5.06%
- **Annualized Volatility:** 27.94%

## Risk-Adjusted Return Metrics
- **Sharpe Ratio:** 0.18
- **Sortino Ratio:** 0.28
- **Calmar Ratio:** 0.12

## Drawdowns
- **Maximum Drawdown:** -43.16%
- **Average Drawdown:** -6.05%
- **Maximum Drawdown Duration:** 1223 days
- **Average Drawdown Duration:** 98 days

## Trading Performance
- **Total Trades:** 82
- **Win Rate:** 45.12%
- **Best Trade:** +30.76%
- **Worst Trade:** -12.95%
- **Average Trade:** +0.48%

## Trade Durations
- **Maximum Trade Duration:** 153 days
- **Average Trade Duration:** 35 days

## Profitability Metrics
- **Profit Factor:** 1.33
- **Expectancy:** 0.74%
- **System Quality Number (SQN):** 0.64

## Strategy Details
- **Strategy:** SMA (Simple Moving Average)
- **Equity Curve & Trade Data:** Detailed data available.

## Summary
- The strategy experienced a moderate return of 48.40% over nearly 8 years, underperforming the significant 583.74% buy-and-hold return.
- Despite a high market exposure, annualized returns were modest at 5.06% with relatively high annual volatility.
- Risk-adjusted return metrics indicate limited efficiency in generating excess returns for the risk taken.
- Drawdown metrics show significant value fluctuations, with a maximum drawdown of over 43%.
- Trading performance was moderately successful, with a win rate of 45.12% and a profit factor of 1.33.
- The strategy, based on a Simple Moving Average (SMA) approach, may benefit from review and adjustments to improve returns and reduce volatility.


## Conclusion
The Trading Risk Profiler is tailored for both beginners and experienced traders, aiming to make algorithmic trading more accessible by aligning strategies with individual risk profiles.

# Libraries and Tools Used in the Project

## Data Handling and Analysis
- **yfinance (`yf`):** Used for fetching historical financial data.
- **Pandas (`pd`):** Essential for data manipulation and analysis.
- **NumPy (`np`):** Fundamental package for scientific computing with Python.

## Visualization
- **hvplot.pandas:** Interactive plotting for Pandas objects using HoloViews.
- **HoloViews (`hv`):** For building complex visualizations easily.
- **Matplotlib (`plt`):** A comprehensive library for creating static, animated, and interactive visualizations.
- **mplfinance (`mpf`):** Specialized for financial data visualization.

## Algorithmic Trading and Backtesting
- **Backtesting:** For testing trading strategies on historical data.
- **TA (Technical Analysis Library):** Provides tools for financial analysis.
- **QuantConnect:** Utilized for paper trading and visualization of trading algorithms.

## Machine Learning
- **Scikit-learn (`sklearn`):**
  - **SVM (Support Vector Machine):** For building and optimizing the trading model.
  - **StandardScaler:** For feature scaling.
  - **train_test_split:** To split data into training and testing sets.
  - **GridSearchCV:** For hyperparameter tuning.
- **PyTorch:** Advanced machine learning library, used for predictive modeling.

## Miscellaneous
- **pandas.tseries.offsets (DateOffset):** For manipulating datetime objects.
- **pathlib (Path):** For filesystem path handling.


---
# Team Responsibilities Overview

## Project Members and Their Roles

- **Jacob & Richard**
  - SMA & Price Crossover Algorithm

- **Richard**
  - Development of Chatbot

- **Dino**
  - Bollinger Bands & RSI Algorithms

## Presentation
- **Contributors:** All members of the group participated in the making of the presentation.


Your feedback and contributions to this project are welcome and appreciated!


