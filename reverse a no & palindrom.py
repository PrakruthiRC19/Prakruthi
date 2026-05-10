#REVERSE A NO

n=3721
new=0
save=n
while(n!=0):
    r=n%10
    n=n//10
    new=new*10
    new=new+r
print(save) # 3721
print(new) # 1273

#PALINDROM

num=1221
start=0
save=num
while(n!=0):
    r=n%10
    n=n//10
    start=start*10
    start=start+r
if save == num:
    print("Palindrom") # 1221=1221 palindrom
else:
    print("Not a Palindrom")
