print("APPEND()")

x=[1,2,3]

x.append(4)
print(x)

print("EXTEND()") # 1 list into another list 

y=['a','b','c']
x.extend(y)
print(x)

print("INSERT()")

z=[1,2,3]
z.insert(2,4)
print(z)

print("REMOVE()")

a=[1,2,3,4,2,5,]
a.remove(2)
print(a)

print("POP()")

b=[1,2,3,4,2,5]
b.pop() # remove last element
print(b)
b.pop(4) # remove element by index
print(b)

print("CLEAR()")

c=[1,2,3,4,5]
c.clear()
print(c)

print("INDEX()")

d=['a','b','c','d','a','c','f']
print(d.index('c'))

print("COUNT()")

print(d.count('c'))

print("SORT()")

d.sort()
print(d)

print("REVERSE()")

d.reverse()
print(d)

print("COPY()")

e=['aa','bb','cc','dd']
f=e.copy()
print("e elements copy to f", f)

print("LEN()")

print(len(e))

print("MAX()")

g=[24,36,64,68,52,26,63]
print(max(g))

print("MIN()")

print(min(g))