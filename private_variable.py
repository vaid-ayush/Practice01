class Variable():
    def __init__(self,public,private):
        self.public=public
        self.__private=private
        

variable= Variable("Public Variable","Private variable")
print(variable.public)
#print(variable.__private)    
'''This will give error as private variable cannot be accessible outside its class'''
print(variable._Variable__private)