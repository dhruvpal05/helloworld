dict={}
for i in range(5):
    key=input("enter key of dictionary:")
    value=input("enter value of dictionary:")
    dict[key] = value
print(dict)
while True:
    print("1.add a new item to dictionary")
    print("2.modify item of dictionary")
    print("3.show all keys")
    print("4.show all values")
    print("5.convert into list")
    print("6.to delete the dictionary")
    print("7.to clear all items of dictonary")
    print("8.show dictionary")

    choice=int(input("enter your choice:"))
    if choice==1:
        new_key=input("enter the key you wanna add")
        new_value=input("enter the value of the key:")
        dict[new_key]=new_value
    elif choice==2:
        print(dict.keys())
        key_=input("enter the key wanna modify:")
        value_=input(":enter new value of the key")
        dict[key_]=value_
    elif choice==3:
        dict.keys()
    elif choice==4:
        dict.values()
    elif choice==5:
        dict.items()
    elif choice==6:
        del dict
    elif choice==7:
        dict.clear()
    elif choice==8:
        print(dict)
    else:
        print("enter valid input!!")
        break