# Functions for EDA and visualization
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller

def plot_price_series(df, title="Brent Oil Prices"):
    df["Price"].plot(figsize=(14, 6), title=title, ylabel="USD per Barrel", grid=True)
    plt.show()

def plot_log_returns(df, title="Log Returns of Brent Oil Prices"):
    df["Log_Returns"].plot(figsize=(14, 4), title=title, ylabel="Log Return", grid=True)
    plt.show()

def adf_test(series, label):
    """Perform ADF test and print results."""
    result = adfuller(series)
    print(f"ADF Test on {label}:")
    print(f"  ADF Statistic: {result[0]:.4f}")
    print(f"  p-value: {result[1]:.4f}")
    print("  Stationary" if result[1] < 0.05 else "  Non-stationary")
