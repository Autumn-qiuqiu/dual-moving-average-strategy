# dual-moving-average-strategy
A simple moving average crossover strategy for QQQ/VOO backtesting

# Dual Moving Average Crossover Strategy
A momentum-based trading strategy for QQQ/VOO using 20-day and 60-day moving averages.

## What it does
- Downloads historical price data via yfinance
- Generates buy/sell signals based on MA crossover
- Backtests strategy performance vs buy-and-hold
- Visualizes cumulative returns and signals

## Results
- Tested on QQQ (2018–2024)
- Compared against S&P 500 benchmark

## Tech Stack
Python | pandas | yfinance | matplotlib

## How to run
pip install yfinance pandas matplotlib
python strategy.py
