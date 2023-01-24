list=[]
n = input("no of ele,elements")
for i in range(n):
    a = int(input("enter elements of list"))
    list.append(a)
m = max(list)
list.remove(m)
m2 = max(list)
print(m2)