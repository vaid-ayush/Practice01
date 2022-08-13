import pandas as pd
  
dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["BCA", "BCA", "M.Tech", "BCA"],
        'score':[90, 40, 80, 98]}

df = pd.DataFrame(dict)
print(df["degree"]== "BCA")
        