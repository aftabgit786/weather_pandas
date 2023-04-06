import pandas as pd

data = pd.read_csv('f2.csv')

events = data[data[' Events'].isin(['Snow', 'Rain', 'Rain-Snow'])]['PKT']

print(events)
