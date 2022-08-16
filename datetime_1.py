import pandas as pd
 
url = 'http://bit.ly/uforeports'

df = pd.read_csv(url)
print(df.head())
df['Time'] = pd.to_datetime(df.Time)

res = df.head()
print(res)