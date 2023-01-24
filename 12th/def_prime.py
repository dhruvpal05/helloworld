def prime(x):
    a=0
    for i in range(1,x+1):
        if x%i==0:
            a+=1
        else:
            pass
    if a==2:
        print('true')
    else:
        print('false')
x=int(input("enter number"))
prime(x)
