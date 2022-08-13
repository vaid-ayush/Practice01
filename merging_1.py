import pandas as pd

data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']} 
   

data2 = {'Name':['Abhi', 'Ayushi', 'Dhiraj', 'Hitesh'], 
        'Age':[17, 14, 12, 52], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']} 

df = pd.DataFrame(data1, index=[0,1,2,3])
df1 = pd.DataFrame(data2, index=[4,5,6,7])

res = pd.concat([df,df1],join='inner')
res1 = pd.concat([df,df1])
print(res)
print(res1)

equ = res1.equals(res)
print(equ)
