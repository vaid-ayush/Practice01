import pandas as pd
import re

data = pd.read_csv("nba-2.csv")

res = data.dropna(inplace=True)
include = ['int','float','object']

desc = data.describe(include=include)
print(desc)