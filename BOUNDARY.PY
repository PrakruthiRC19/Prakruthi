# BOUNDARY

n=9
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        if (i==1 or i==n or j==1 or j==n):
            print("* ",end="")
        else:
            print("  ",end="")
    print(" ")

print("\n")
# DIAGONAL

n=9
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        if (i==j or i==n or j==1):
            print("* ",end="")
        else:
            print("  ",end="")
    print(" ")

print("\n")

n=9
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        if (i+j==n+1 or i==n or j==n):
            print("* ",end="")
        else:
            print("  ",end="")
    print(" ")

print("\n")

n=9
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        if (i==1 or j==1 or j==5 or i==n or j==n):
            print("* ",end="")
        else:
            print("  ",end="")
    print(" ")

print("\n")

n=9
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        if (j==1 or j==n or i==j or i+j==n+1):
            print("* ",end="")
        else:
            print("  ",end="")
    print(" ")

print("\n")

n=9
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        if (i==5 or j==5 or i==j or i+j==n+1):
            print("* ",end="")
        else:
            print("  ",end="")
    print(" ")

print("\n")

n=9
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        if (i+j==n+1-4 or i+j==n+1+4 or i==j-4 or i==j+4):
            print("* ",end="")
        else:
            print("  ",end="")
    print(" ")