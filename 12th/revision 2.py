'''def Readfile():
    i = open("Employee.dat","rb+")
    x = i.readline()
    while(x):
        I=x.split(':')
        if (20000>=float(I[2])<=5000):
            print(x)
            x = i.readline()'''

''''N=[12, 13, 34, 56, 21, 79, 98, 22, 35, 38]
s=[]

def push(s,N):
    for i in N:
        if i%2==0:
            s.append(i)
        else:
            pass
push(s,N)
print(s)



def pop(N):
    for i in range(len(N)):
        print(N.pop(),end=" ")

pop(N)'''

r={"OM":76, "JAI":45, "BOB":89, "ALI":65, "ANU":90,"TOM":82}
list=[]

def push(a,b):
    for i in a:
        if a[i]>75:
            b.append(i)
        else:
            pass

push(r,list)
print(list)

def pop(a):
    for i in range(len(a)):
        if len(a)==0:
            break
        else:
            print(a.pop(),end=" ")

pop(list)
