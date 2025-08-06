import matplotlib.pyplot as plt

def plot_with_change_point(df, trace):
    τ_samples = trace.posterior['τ'].values.flatten()
    τ_mean = int(τ_samples.mean())
    change_date = df.iloc[τ_mean]['Date']

    plt.figure(figsize=(14, 5))
    plt.plot(df['Date'], df['LogReturn'], label='Log Return')
    plt.axvline(change_date, color='red', linestyle='--', label=f'Change Point ≈ {change_date.date()}')
    plt.title('Detected Change Point in Log Returns')
    plt.xlabel('Date')
    plt.ylabel('Log Return')
    plt.legend()
    plt.grid(True)
    plt.show()

    return change_date
