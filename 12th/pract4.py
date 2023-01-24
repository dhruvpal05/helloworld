x=[]
y=[]
z=[]
a=int(input('range of list:'))

for i in range(a):
    b=int(input("enter elements of list"))
    x.append(b)
print(x)
for j in x:
    if j>0:
        y.append(j)
    else:
        z.append(j)

print(y)
print(z)