#Enter the currency pair
currency_pairs = [
 "USDCHF=X", "USDNOK=X"
]
start_date = '2021-01-01'
end_date = '2021-12-30'

forex_data = pd.DataFrame()
for currency_pair in currency_pairs:
    
    data = yf.download(currency_pair, start=start_date, end=end_date)['Adj Close']
    data.rename(currency_pair, inplace=True)
    forex_data = pd.concat([forex_data, data], axis=1)
    forex_data.dropna(inplace=True)

X = forex_data['USDCHF=X']
y = forex_data['USDNOK=X']

# Fitting the regression model
X = sm.add_constant(X)  
model = sm.OLS(y, X)
results = model.fit()

# calculating residuals and z-score
predicted_values = results.predict(X)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
Residuals = y - predicted_values

# Perform ADF test on residuals
adf_result = adfuller(Residuals)

# Extract ADF test statistic and p-value
adf_statistic = adf_result[0]
p_value = adf_result[1]
if adf_statistic < adf_result[4]['5%'] and p_value < 0.05:
    print("Reject the null hypothesis. Residuals are stationary.")
else:
    print("Fail to reject the null hypothesis. Residuals are non-stationary.")

forex_data['Residuals']=Residuals    
# Calculate z-scores
mean_u = np.mean(forex_data['Residuals'])
std_u = np.std(forex_data['Residuals'])
forex_data['Z-Score'] = (forex_data['Residuals'] - mean_u) / std_u

Signal=[]
for x in forex_data['Residuals']:
    if x > 1:
        Signal.append("short USDCHF,long USDNOK")
    if x < 1:
        Signal.append("long USDCHF,short USDNOK")
forex_data['Signal']=Signal
