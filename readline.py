import linecache


with open("lines.txt",'w') as text:
    text.write("This is line 1 \n This is line 2 \n This is line 3 \n This is line 4 \n This is line 5 \n")

with open("lines.txt",'r') as text:
    content = text.readlines()
    print("Print 4th line")
    print(content[3])

with open("lines.txt",'r') as text:
    content=text.readlines()
    print(content[0:2])


particular_line=linecache.getline("lines.txt",2)    
print(particular_line)

with open("lines.txt",'r') as text:
    lines=[0,2,3]
    for pos,line_num in enumerate(text):
        if pos in lines:
            print(line_num)
