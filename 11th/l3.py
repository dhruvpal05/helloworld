n1=int(input("1st number"))
n2=int(input("2nd number"))
n3=int(input("3rd number"))
if n1>n2 and n2>n3:
    print(n1,n2,n3)
elif n1>n3 and n3>n2:
    print(n1,n3,n2)
elif n2>n1 and n1>n3:
    print(n2,n1,n3)
elif n2>n3 and n3>n1:
    print(n2,n3,n1)
elif n3>n1 and n1>n2:
    print(n3,n1,n2)
else:
    print(n3,n2,n1)