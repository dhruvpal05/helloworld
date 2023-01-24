def amount(a):
    b = input("are you member of store(yes or no)")
    if b in "yes":
        z = a * (1 / 20)
    else:
        pass
    if a>=500 and a<1000:
        a=a-a*(1/20)-z
    elif a>=1000 and a<2000:
        a=a-a*(8/100)-z
    elif a>=2000:
        a=a-a*(1/10)-z
    else:
        pass

    return a


a=int(input("enter money:"))
print("net payable amount=",amount(a))
