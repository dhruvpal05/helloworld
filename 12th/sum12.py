import pickle
lst=[]
a=int(input("no of emp?"))
for i in range(a):
    Empno=int(input('enter emp no'))
    Ename=input("enter name")
    post=input("enter post")
    salary=int(input("enter salary"))
    lst.append([Empno,Ename,post,salary])

def NewEmp():
    file1=open('EMP.dat','wb')
    pickle.dump(lst,file1)
    file1.close()

def display():
    file1=open("EMP.dat","rb")
    data=pickle.load(file1)
    print(data)


NewEmp()
display()
