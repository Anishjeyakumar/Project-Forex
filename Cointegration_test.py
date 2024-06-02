import pandas as pd
import yfinance as yf
import statsmodels.api as sm

#enter the currencies to perform cointegration test
currency_pairs =[""]
#enter start and end dates
start_date = ''
end_date = ''
#to fetch data
forex_data = pd.DataFrame()
for currency_pair in currency_pairs:
    data = yf.download(currency_pair, start=start_date, end=end_date)['Adj Close']
    data.rename(currency_pair, inplace=True)
    forex_data = pd.concat([forex_data, data], axis=1)
    forex_data.dropna(inplace=True)

#returns a csv with cointegration results
results_list = []
for pair in currency_pairs:
    x = forex_data[pair]
    for other_pair in currency_pairs:
        if other_pair != pair:
            y = forex_data[other_pair]
            eg_results = sm.tsa.stattools.coint(x, y, trend='c', method='aeg', maxlag=None, autolag='aic', return_results=True)
            p_value = "{:.5f}".format(eg_results[1])  # Format p-value to display in 0.xx format
            if float(p_value) < 0.05:
                cointegration = 'Cointegrated'
            else:
                cointegration = 'Non-Cointegrated'
            results_list.append({'Currency Pair 1': pair, 'Currency Pair 2': other_pair, 'P-Value': p_value, 'Cointegration': cointegration})
results_df = pd.DataFrame(results_list)
results_df.to_csv('C:/Quant/CSV/cointegration_results.csv', index=False)
