'''N=[12, 13, 34, 56, 21, 79, 98, 22, 35, 38]
stack=[]
def pusheven(n):
    for i in n:
        if i%2==0:
            stack.append(i)
        else:
            pass
def pop():
    for i in range(len(stack)):
        print(stack.pop(),"del item")


pusheven(N)
print(stack)
pop()'''

R={"OM":76, "JAI":45, "BOB":89, "ALI":65, "ANU":90,
"TOM":82}
stack=[]
def push(r):
    for i in r:
        if i.values > 75:
            stack.append(i)
        else:
            pass
def pop():
    for i in range(len(stack)):
        print(stack.pop())

push(R)
print(stack)
pop()


