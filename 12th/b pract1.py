''''''


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

def sum_salary(post):
    file1=open('EMP.dat','rb')
    sum=0
    lst=pickle.load(file1)
    for i in lst:
        if i[2]==post:
            sum=sum+i[3]
    print(sum)
    file1.close()

NewEmp()
post=input("enter the name of post to check salary")
sum_salary(post)

