while True:
    print("1. to do something good")
    print("2. to do something bad")
    print("3. to exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        print("good")
    elif choice==2:
        print("bad")
    elif choice==3:
        break
    else:
        print("enter valid input!!")