'''def push(pname):
    if pname[0]=='D':
        print("hell")

push("Dhell")'''

stack=[1,2,3,4,5,6,7,8]

'''def peek(a):
    if len(a)==0:
        print("empty stack")
    else:
        print(a[-1])
peek(stack)

def push(a):
    x=int(input("enter element"))

    a.append(x)
    print(a)
push(stack)

def pop(a):
    if len(a) == 0:
        print("empty stack")
    else:
        print(a.pop())
pop(stack)'''

def display(a):
    for i in range(len(a)-1,-1,-1):
        print(a[i],end="")

display(stack)





