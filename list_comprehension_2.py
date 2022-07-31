txn=[24.6,45.7,25,12,78,9.7]

rate=0.8

def get_price(t):
    return t*(1+rate)

final=[get_price(i) for i in txn]    
print(final)
