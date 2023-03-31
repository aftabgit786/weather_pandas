import pandas as pd

data = pd.read_csv('f2.csv')

get_events = data[' Events']

events = data[get_events.isin(["Rain",  "Snow",  "Rain-Snow"])]

print(events[' Events'])
