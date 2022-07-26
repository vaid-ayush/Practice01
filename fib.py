def fib(n):
    result=[]
    a=0
    b=1
    while b<n:
        result.append(a)
        a,b=b,a+b
        print(a,end=' ')

fib(2000)        