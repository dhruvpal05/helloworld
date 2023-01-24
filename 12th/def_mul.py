def multiply(x):
    a=x[0]
    for i in range(1,len(x)):
        a=a*x[i]
    return a
lis=[8, 2, 3, -1, 7]
print(multiply(lis))



