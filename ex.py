a= int(input("Enter the range"))
print("Number of prime numbers upto",a)
for n in range(2,a):
    for x in range(2,n):
        if n%x==0:
            print(n,'equals',x,'*',n//x)
            break
    else:
            print(n,'is prime number')
