def factorial(x):
    c=0
    for i in range(x):
        c=x*(x-1)

    return c


x=int(input("enter number"))
print(factorial(x))