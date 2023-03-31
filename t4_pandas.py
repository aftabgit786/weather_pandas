import pandas as pd

data = pd.read_csv('f2.csv')

thunderstorm_data = data[data[' Events'] == 'Thunderstorm']
date = pd.to_datetime(thunderstorm_data['PKT'])
day_names = date.dt.strftime('%A')

print(day_names)
