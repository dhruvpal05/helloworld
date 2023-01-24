x=int(input("enter number"))
if x>1:
    for i in range(2,x):
        if x%i==0:
            print("it is not a prime number")
            break
        else:
            print("it is a prime number!!")
            break
else:
    print("it is not a prime number")