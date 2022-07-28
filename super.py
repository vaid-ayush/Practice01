class Emp():
    def __init__(self,name,id):
        self.name=name
        self.id=id

class detail(Emp):
    def __init__(self,name,id,emailid):
        super().__init__(name,id)
        self.emailid=emailid

employee_1=detail("Ayush","5005","ayushvaid@gmail.com")
print("The name is ",employee_1.name)
print("ID no is ", employee_1.id)
print("EmailID is ",employee_1.emailid)
