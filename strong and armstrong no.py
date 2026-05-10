def fact(n):
    f=1
    for i in range(1,n+1,1):
        f=f*i
    return f

num=145
save=num
sum=0
while num!=0:
    r=num%10
    num=num//10
    sum=sum+fact(r)

if save==sum:
    print("Strong NO")
else:
    print("Not a strong no")

# ARMSTRONG NO

n=153
save=n
sum=0
count=len(str(n))
while(n!=0):
    r=n%10
    n=n//10
    sum=sum+(r**count)
if sum==save:
    print("Arm Strong Number")
else:
    print("Not Arm Strong Number")