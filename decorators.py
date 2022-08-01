def print_twice(func):
    def wrapper_twice(*args,**kwargs):
        func(*args,**kwargs)
        func(*args,**kwargs)
    return wrapper_twice

@print_twice
def greetings(name):
    print("Hello",name)

a=greetings("Ayush")           