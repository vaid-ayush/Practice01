import pandas as pd

data = pd.read_csv("nba-2.csv")
df = data.head(10)
print(df)