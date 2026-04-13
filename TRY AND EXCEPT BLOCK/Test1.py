class Test1:

    a=int(input("Enter the value of a:"))
    b=int(input("Enter the value of b:"))

    def divide(self):
        
        try:

            c=Test1.a/Test1.b  # RISKIER 

        except ZeroDivisionError:

            print("Please enter a valid denominator")

        except Exception:
            
            print("if noting is work.i will work")

t=Test1()
t.divide()