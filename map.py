def reverse(s):
    return s[::-1]
    
sports=["cricket","badminton","hockey","chess"]
iterate=map(reverse,sports)
for i in iterate:
    print(i)
