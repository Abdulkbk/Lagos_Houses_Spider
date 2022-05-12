import pandas as pd

df = pd.read_csv('../../lagos_houses.csv', header=None)

print(df.head())

df.to_csv('../data/lagos_houses.csv', header=['beds', 'bathrooms', 'toilets', 'parking_space', 'title', 'state', 'price'], index=False)