print("CUTTING THE STARS\n")

n=5
for i in range(1,5+1,1):
    for j in range(1,i+1,1):
        print("*",end="")
    print("")

print("\n2 to 6\n")

n=5
for i in range(1,5+1,1):
    for j in range(1,i+1+1,1):
        print("*",end="")
    print("")

print("\n1 to 4\n")

n=5
for i in range(1,5+1,1):
    for j in range(1,i-1+1,1):
        print("*",end="")
    print("")

print("\nodd\n")

n=4
for i in range(1,4+1,1):
    for j in range(1,(n+i)-(n-i)-1+1,1):
        print("*",end="")
    print("")

print("\neven\n")

n=4
for i in range(1,4+1,1):
    for j in range(1,(n+i)-(n-i)+1,1):
        print("*",end="")
    print("")
