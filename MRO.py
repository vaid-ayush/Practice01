class A:
    def a(self):
        print("In class A")


class B:
    def a(self):
        print("In class B")


class C(A,B):
    def a(self):
        print("In class C")

r=C()

print(C.__mro__)
print(C.mro())
