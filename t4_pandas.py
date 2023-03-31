import pandas as pd

data = pd.read_csv('f2.csv')

get_thunderstorm = data[data[' Events'] == 'Thunderstorm']
date = pd.to_datetime(get_thunderstorm['PKT'])
day_names = date.dt.strftime('%A')

print(day_names)
