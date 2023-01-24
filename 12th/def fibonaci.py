def fibo():
    a=int(input("enter nummber"))
    x=0
    y=1
    z=0
    while z<=a:
        print(z)
        x=y
        y=z
        z=x+y
fibo()

range(10:20:2)