def fact(n):
    fact=1
    for i in range(1,n+1,1):
        f=fact*i
    return f

num=145
save=num
sum=0
while(num!=0):
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
count=0
while(n!=0):
    r=n%10
    n=n//10
    count=count+1
    sum=sum+(r**count)
if sum==save:
    print("ASN")
else:
    print("NASN")