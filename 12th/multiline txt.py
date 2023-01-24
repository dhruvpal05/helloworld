with open("multi.txt","w") as file:
    list1=[]
    while True:
        a=input("enter one line text")
        list1.append(a)
        x=input("want to enter more(y/n)")
        if x in "nN":
            break
    print(list1)