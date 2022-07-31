def reverse(s):
    return s[::-1]


print(reverse("I have joined Shorthills tech"))

reverse= lambda s: s[::-1]
print(reverse("I have joined Shorthills tech"))    
print((lambda s:s[::-1])("I have joined Shorthills tech"))