import pandas as pd
 
# importing numpy as np
import numpy as np
  
# Define a dictionary containing employee data
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
#grp = df.groupby(["Name","Qualification"])
print(grp.agg({"Age":"sum", "Score": "std"}))