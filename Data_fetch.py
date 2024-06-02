import yfinance as yf
import pandas as pd

#enter the currencies to fetch data
currency_pairs = [
    ""
]

#enter start and end date
start_date = ''
end_date = ''

forex_data = pd.DataFrame()
for currency_pair in currency_pairs:
    
    data = yf.download(currency_pair, start=start_date, end=end_date)['Adj Close']
    data.rename(currency_pair, inplace=True)
    forex_data = pd.concat([forex_data, data], axis=1)
    forex_data.dropna(inplace=True)

print(forex_data)
