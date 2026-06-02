import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# 下载数据
ticker = "QQQ"
df = yf.download(ticker, start="2018-01-01", end="2024-01-01")
df = df[["Close"]].copy()

# 计算移动平均线
df["MA20"] = df["Close"].rolling(20).mean()
df["MA60"] = df["Close"].rolling(60).mean()

# 生成信号
df["Signal"] = 0
df.loc[df["MA20"] > df["MA60"], "Signal"] = 1   # 持有
df.loc[df["MA20"] < df["MA60"], "Signal"] = -1  # 空仓

# 计算收益
df["Return"] = df["Close"].pct_change()
df["Strategy"] = df["Signal"].shift(1) * df["Return"]

# 累计收益
df["Cumulative_Market"] = (1 + df["Return"]).cumprod()
df["Cumulative_Strategy"] = (1 + df["Strategy"]).cumprod()

# 可视化
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

ax1.plot(df["Close"], label="Price", alpha=0.7)
ax1.plot(df["MA20"], label="MA20", alpha=0.8)
ax1.plot(df["MA60"], label="MA60", alpha=0.8)
ax1.set_title(f"{ticker} Moving Average Crossover")
ax1.legend()

ax2.plot(df["Cumulative_Market"], label="Buy & Hold")
ax2.plot(df["Cumulative_Strategy"], label="MA Strategy")
ax2.set_title("Cumulative Returns")
ax2.legend()

plt.tight_layout()
plt.show()

# 简单统计
print(f"最终市场收益: {df['Cumulative_Market'].iloc[-1]:.2f}x")
print(f"最终策略收益: {df['Cumulative_Strategy'].iloc[-1]:.2f}x")
sharpe = df["Strategy"].mean() / df["Strategy"].std() * (252**0.5)
print(f"策略Sharpe Ratio: {sharpe:.2f}")
