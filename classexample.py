class person():
    def __init__(self,name,age,occupation):
        self.name=name
        self.age=age
        self.occupation=occupation

    def show(self):
        print("Name is:",self.name)
        print("Age is:",self.age)
        print("Occupation is:",self.occupation)

ayush = person("ayush vaid","26","SDE")
sanchit = person("Sanchit","28","Digital Marketing")
Kartik = person("Kartik","24","Graphic Designer")

ayush.show()
sanchit.show()
Kartik.show()

