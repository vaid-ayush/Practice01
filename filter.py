def greater(x):
    return x>100

g=filter(greater,[1,2,4,5,7,100,2333,4533,6768,2345])
for i in g:
    print(i)    