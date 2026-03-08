class A:
    def display(self):
        print("A is displaying")

class B(A):
    def run(self):
        print("B is running")

class C(A):
    def runner(self):
        print("C is runner")

class D(B,C):
    def player(self):
        print("D is player")

print("**D's property**")
d=D()
d.player()
d.runner()
d.run()
d.display()
print("**C's property**")
c=C()
c.runner()
c.display()
print("**B's property**")
b=B()
b.run()
b.display()
print("**A's property**")
a=A()
a.display()
