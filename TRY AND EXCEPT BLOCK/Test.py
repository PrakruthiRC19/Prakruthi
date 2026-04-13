class Test:

    a=int(input("Enter the value of a:"))
    b=int(input("Enter the value of b:"))

    def divide(self):
        
        try:

            c=Test.a/Test.b  # RISKIER 
            '''
            Enter the value of a:20 
            Enter the value of b:5 
            4.0'''
            print(c) 

        except ZeroDivisionError: 
            '''
        exception name must matched with try block problem 
        '''

            print("Please enter a valid denominator")  # SOLUTION 
'''
Enter the value of a:30
Enter the value of b:0
Please enter a valid denominator'''

t=Test()
t.divide()