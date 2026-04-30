# FIND THE FACTORS OF NUMBER

n=10
for i in range(1,n+1,1):
    if n%i==0:
        print(i)

print("\n")

# COUNT THE FACTORS OF NUMBER

n=11
count=0
for i in range(1,n+1,1):
    if n%i==0:
        count=count+1

print(count)

print("\n")

# PROGRAM TO FIND PRIME NO
n=88
count=0
for i in range(1,n+1,1):
    if n%i==0:
        count=count+1
if count==2:
    print("Prime no")
else:
    print("not a prime")

               