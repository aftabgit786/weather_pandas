import pandas as pd

data = pd.read_csv('f1.csv')

max_temperature = data['Max TemperatureC']
min_temperature = data['Min TemperatureC']

average = (max_temperature - min_temperature) / 2

print(average)
