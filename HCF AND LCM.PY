# HCF

a=10
b=60
HCF=0
for i in range(1,a+1,1):
    if a%i==0 and b%i==0:
        HCF=i
print("HCF",HCF)

print("\n")

#LCM

a=20
b=70
HCF=0
for i in range(1,a+1,1):
    if a%i==0 and b%i==0:
        HCF=i
print("HCF",HCF)
LCM=a*b//HCF
print("LCM",LCM)
        
