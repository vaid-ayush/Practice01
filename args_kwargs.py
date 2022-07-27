def fun(*args, **kwargs):
    print(args)

    for k,w in kwargs.items():
        print(k," ",w)

args=["short", "hills","tech","Gurgaon"]
kwargs={"firstname":"Ayush","middle name":"None","Lastname":"Vaid"}
fun(*args)
fun(**kwargs)            