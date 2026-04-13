class Calculate:

    def divide(Self,b):

        try:

            a=int(input("Please enter a value of a"))
            # print("I'm in the outer try block")

            try:

                c=a/b
                print(c)

            except ZeroDivisionError:

                print("Denominator cannot be zero")

        except Exception:

            print("please entry any number")
            # print("All is well")

c=Calculate()
c.divide(10)