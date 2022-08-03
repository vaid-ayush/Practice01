from decimal import DivisionByZero


def divbyzero():
    x=1/0

try:
    divbyzero()
except DivisionByZero as err:
    print("handling run time error",err)        