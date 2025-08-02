# Functions for loading and preparing data
import pandas as pd
import numpy as np  # Import NumPy

def load_brent_data(file_path: str) -> pd.DataFrame:
    """Loads and cleans Brent Oil Price data."""
    df = pd.read_csv(file_path)
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")  # Convert Date column to datetime
    df = df.dropna(subset=["Date"])  # Drop rows where Date is NaT
    df = df.sort_values("Date").set_index("Date")  # Sort by Date and set as index
    return df

def compute_log_returns(df: pd.DataFrame) -> pd.DataFrame:
    """Computes log returns and drops NA."""
    df["Log_Returns"] = (df["Price"] / df["Price"].shift(1)).apply(np.log)  # Compute log returns
    return df.dropna()  # Drop rows with NA values