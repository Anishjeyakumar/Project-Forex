initial_cash = 100000
position_size = 1000

cash = initial_cash
positions = 0

for i in range(len(signals)):
    if signals[i] == 1:
        positions += position_size
        cash -= data['GBPUSD=X'][i] * position_size
    elif signals[i] == -1:
        positions -= position_size
        cash += data['GBPUSD=X'][i] * position_size

final_value = cash + positions * data['GBPUSD=X'].iloc[-1]
print(f'Final portfolio value: {final_value}')
