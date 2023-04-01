import pandas as pd

data = pd.read_csv('f2.csv')

data_thunderstorm = data[data[' Events'] == 'Thunderstorm']
date = pd.to_datetime(data_thunderstorm['PKT'])
day_names = date.dt.strftime('%A')

print(day_names)
