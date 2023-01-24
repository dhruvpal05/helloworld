list=[1,2,3,4,5,6,7,8,9,0]
print(list)
while True:
    print("1.append an element:")
    print("2.insert an element:")
    print("3.append a list to a list:")
    print("4.modify an existing element:")
    print("5.delete element from position:")
    print("6.delete element with given value:")
    print("7.sort list in ascending order:")
    print("8.sort list in descending order:")
    print("9.display the list:")

    choice=int(input("enter your choice:"))
    if choice==1:
        element=int(input("enter element"))
        list.append(element)
    elif choice==2:
        element=int(input("enter element:"))
        position=int(input("enter its position"))
        list.insert(position,element)
    elif choice==3:
        list1=[]
        for i in range(3):
            i = int(input("enter elements of 2nd list:"))
        list.insert(list1)
    elif choice==4:
        i=int(input("enter the position of the element:"))
        if i > len(list):
            new=int(input("enter new element:"))
            old=list[i]
    elif choice==6:
        i=int(input("enter element want to remove:"))
        list.remove(i)
    elif choice==5:
        i=int(input("enter position of the value to be removed:"))
        if i< len(list):
            list.pop(i)
        else: 
            print("invalid index number:") 
    elif choice==7:
        list.sort()
    elif choice==8:
        list.sort(reverse=True)
    elif choice==9:
        print(list)
    else:
        print("enter valid input:")
    break
print(list)