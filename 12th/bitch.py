'''WAp Program to create CSV file and store empno,name,salary.\n
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
file1=open("compan.csv","w")
data=csv.writer(file1)
data.writerows(lis1)
file1.close()
print("data written")

file1=open("compan.csv","r")
data=csv.reader(file1)
while True:
    s=int(input("emp no to be searched "))
    found=0
    for i in data:
        if len(i) != 0:
            if int(i[0]) == s:
                print(i)
                found += 1
                break
    if found==0:
        print("data not found ")
        break
    break
















