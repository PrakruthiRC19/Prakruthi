class divide:

    def division(self,a,b):
        
        try:
            c=a/b
            print(c)

        except ArithmeticError:
            print("please don't entry denominator zero ")

        except Exception:
            print("typeerror:both input must be number")

        except ZeroDivisionError:
            print("please entry denominator as whole number ")

d=divide()
d.division(10,20)