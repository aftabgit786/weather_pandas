import pandas as pd

data = pd.read_csv('f2.csv')

events = data[' Events']

get_events = data[events.isin(["Rain",  "Snow",  "Rain-Snow"])]

print(get_events[' Events'])
