class Calculate1:

    def add(self): #method overloading
        x=10
        y=20
        z=x+y
        print(z)

    def add(self,a,b):
        return (a+b) # if we want to return the statement , we need to invote retrurn in print statement.
                     # assign method caller to variable and invoke that variable.
    
    def add(self,x,y):
        a=x
        b=y
        c=a+b
        print(c)
    
c=Calculate1()
c.add(10,20)
