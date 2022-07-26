a=["Chess","Cricket","Badminton","Football","Tennis"]
for i in range(len(a)):
    print(a[i])
    if a[i]=="Football":
        print("Found Football")
        break
        print("After break it wont print")
print("Loop terminated")

for j in range(len(a)):
    if a[j] == "Badminton":
        continue
    print("Found",a[j])

    