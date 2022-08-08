import pandas as pd
import numpy as np


data = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score':[np.nan, 40, 80, 98]}

df = pd.DataFrame(data)
nul = df.isnull()
print(nul) 
print(df)


#replacing missing data with a value

rep = df.fillna(0)
print(rep)