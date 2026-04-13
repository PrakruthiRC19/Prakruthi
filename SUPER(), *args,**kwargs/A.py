class A:

    def display(self,**kwargs):
        print(kwargs)

a=A()
a.display(id=33, name="prakruthi", contact=9740740742)