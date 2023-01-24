import os
stack=[]
def push():
    a=input("enter the data")
    stack.append(a)
def pop():
    if len(stack)==0:
        print("empty stack")
    else:
        a=stack.pop()
def display():
        print(stack)
while True:
    print("1:To add stack\n2:To delete stack\n3:To display stack\n4:To exit")
    x=int(input("enter your choice:"))
    if x==1:
        push()
    elif x==2:
        pop()
    elif x==3:
        display()
    elif x==4:
        os.sys.exit(0)
    else:
        print("enter valid input")

