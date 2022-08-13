import pandas as pd

data = pd.read_csv("nba-2.csv" , index_col="Name")

df = pd.DataFrame(data)
first = data.loc[["Avery Bradley","R.J. Hunter"]]
second = data.loc[["Avery Bradley","R.J. Hunter"],["Team","Position","Salary"]]

print(first)
print(second)
