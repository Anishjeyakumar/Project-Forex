import yfinance as yf
from statsmodels.tsa.stattools import adfuller
import pandas as pd

currency_pairs = [
   # ""# Enter the currencies-adf test
]
start_date = ""
end_date = ""

adf_r = []
# loop to perform adf test for each pairs and to store in 
for currency_pair in currency_pairs:
    data = yf.download(currency_pair, start=start_date, end=end_date)['Close'].dropna()
    result = adfuller(data)
    test_statistic, p_value, critical_values = result[0], result[1], result[4]
    #set the p-value accordingly
    stationary = 'Stationary' if p_value < 0.05 else 'Non-Stationary'  
    df = pd.DataFrame({'Forex Currency': currency_pair,
                       'Test Statistic': test_statistic,
                       'P-value': p_value,
                       'Critical Value (1%)': critical_values['1%'],
                       'Critical Value (5%)': critical_values['5%'],
                       'Critical Value (10%)': critical_values['10%'],
                       'Stationary': stationary}, index=[0])
    adf_r.append(df)

results_adf = pd.concat(adf_r, ignore_index=True)
print(results_adf)
