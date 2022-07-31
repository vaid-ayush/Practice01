class Employee():
    raise_amt=1.02
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.email=first+'.'+last+'@gmail.com'
        self.pay=pay

    def fullname(self):
        return'{}{}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt=1.10 
    def __init__(self,first,last,pay,language):
        super().__init__(first,last,pay)
        self.language=language


dev_1=Developer("Ayush","Vaid",50000,"Python")
dev_2=Employee("Atul","Choudhary",100000)

print(dev_1.pay)
print(dev_1.language)
dev_1.apply_raise()
print(dev_1.pay)
print(dev_2.pay)
dev_2.apply_raise()
print(dev_2.pay)
print(dev_1.email)
print(dev_2.email)
print(dev_1.fullname())