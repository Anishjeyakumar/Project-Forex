import numpy as np
import pandas as pd
import yfinance as yf
import statsmodels.api as sm

# Fetch historical Forex data
def fetch_data(pairs, start_date, end_date):
    data = yf.download(pairs, start=start_date, end=end_date)
    return data['Adj Close']

# Define the currency pairs and date range
currency_pairs = ['EURUSD=X', 'GBPUSD=X']
start_date = '2023-01-01'
end_date = '2023-01-01'

# Fetch the data
data = fetch_data(currency_pairs, start_date, end_date)

# Handle missing values by dropping rows with NaNs
data = data.dropna()

# Perform OLS regression
X = sm.add_constant(data['EURUSD=X'])
model = sm.OLS(data['GBPUSD=X'], X).fit()
spread = data['GBPUSD=X'] - model.predict(X)

# Trade signals
mean = spread.mean()
std = spread.std()
entry_threshold = 2 * std
exit_threshold = 0.5 * std

signals = np.where(spread > mean + entry_threshold, -1, 0)
signals = np.where(spread < mean - entry_threshold, 1, signals)
signals = np.where(abs(spread - mean) < exit_threshold, 0, signals)

# Output the signals
print("Signals:")
print(signals)

