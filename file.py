with open("diary.txt",'w') as text:
    text.write("Ayush Vaid , From Jammu, living in Gurgaon \n I am an Mtech Graduate from PEC chandigarh \n")

with open("diary.txt",'r') as text:
    text_object = text.read()
    print(text_object)
    
with open("diary.txt",'r') as text:    
    text_object_1=text.readline()
    print(text_object_1)

with open("diary.txt",'a') as text:
    text_object_2 = text.write("appending a second line into existing file")

with open("diary.txt",'r') as text:
    print(text.read())        
