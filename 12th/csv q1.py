'''WAP to create CSV file and store empno,name,salary.\n
 Then search any empno and display name, salary and\n
  if not found display appropriate message'''

import csv
lis1=[]
a=int(input("enter the number of emp"))
for i in range(a):
    empno=int(input("enter emp no"))
    name=input("enter emp name")
    salary=int(input("enter emp salary"))
    lst=[empno,name,salary]
    lis1.append(lst)
file1=open("company.csv","w")
data=csv.writer(file1)
data.writerows(lis1)
file1.close()
print("data written")

file1=open("company.csv","r")
data=csv.reader(file1)
emp_no=int(input("emp no to be searched "))
while True:
    x=0
    for i in data:
        if len(i)!=0:
            if int(i[0])==emp_no:
                print(i)
                x+=1
                break
    if x==0:
        print("data not found ")
        break
    break


'''Write udf in the qustion no1 and count no of employees \n
having salary more than 25000.'''

def count():
    file1=open("company.csv","r")
    data=csv.reader(file1)
    noofemp=0
    while True:
        for i in data:
            if len(i)!=0:
                if int(i[2])>25000:
                    noofemp+=1
        break
    print("no of emp having salary more than 25000 =",noofemp)

count()


