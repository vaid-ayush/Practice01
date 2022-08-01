'''def function():
    print("Ayush Vaid")

func1=function 
del function
func1()
'''
def function1(function2):
    def function3():
        print("Ayush")
        function2()
        print("Vaid")
    return function3

@function1
def function4():
    print("Ayush Vaid")
function4()          
