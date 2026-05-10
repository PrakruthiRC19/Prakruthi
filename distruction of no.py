# EXTRACT ALL DIGITS FROM NO SEPARATLY

n=3721
while(n!=0):
    r=n%10
    n=n//10
    print(r) # 1 , 2 , 7 , 3

# FIND SUM OF DIGITS OF NUMBER

n=1234
sum=0
while(n!=0):
    r=n%10
    n=n//10
    sum=sum+r
print(sum) # 10

#LENGTH OF NO

n=2345
count=0
while(n!=0):
    r=n%10
    n=n//10
    count=count+1
print(count) #4

