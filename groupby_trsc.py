from unittest import result
import pandas as pd
import numpy as np

data1 = {'Name':['Jai', 'Anuj', 'Jai', 'Princi',
                 'Gaurav', 'Anuj', 'Princi', 'Abhi'],
        'Age':[27, 24, 22, 32,
               33, 36, 27, 32],
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj',
                   'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd',
                         'B.Tech', 'B.com', 'Msc', 'MA'],
        'Score': [23, 34, 35, 45, 47, 50, 52, 53]}

df = pd.DataFrame(data1)

grp = df.groupby("Name")
sc = lambda x : (x - x.mean()/x.std() * 10)
reesult = grp.transform(sc)
print(reesult)
