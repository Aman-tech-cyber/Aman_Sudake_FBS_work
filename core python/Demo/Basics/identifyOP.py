x = 10
y = 10
z = 20
 
# 1. is
print(x is y)
print(id(x))
print(x is z)
print(id(z))
li1 = [1,2,3]
li2 = [1,2,3]
print(li1 is li2)
print(id(li1[0]))
print(id(li2[0]))
print(li1[0] is li2[0])