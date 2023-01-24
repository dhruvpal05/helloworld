#write a python to creat a tuple by accepting 10 values from the user and find min and max value
t=tuple()
for i in range(10):
    n =int(input("enter 10 values:"))
    t=t+(n,)
print(t)
print(max(t))
print(min(t))

