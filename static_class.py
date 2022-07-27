from datetime import date

class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def age(cls, name, yob):
        return cls(name, date.today().year-yob)

    @staticmethod
    def adult(age):
        return age>18

person1=Person("Ayush",26)
person2=Person("Sanchit",28)
person3=Person.age("Rahul",1998)

print(person1.name, person1.age)
print(person2.name,person2.age)
print(person3.name,person3.age)

print(Person.adult(22))

