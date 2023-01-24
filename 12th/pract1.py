def count1(x,y):
    c=0
    for i in range(len(x)):
        if x==y:
            c+=1

x=input("enter string:")
y=input("enter character to be searched:")
a=count1(x,y)
print(a)
