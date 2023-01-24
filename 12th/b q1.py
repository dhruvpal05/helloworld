'''wapp to accept product code, name and price.\n
 Write records in binary file and then print that\n
  data of required product code.'''

import pickle

file1=open("new.dat","wb")
a=int(input("how many products"))
lst=[]
for i in range(a):
    list1=[]
    pcode=int(input("enter product code"))
    pname=input("enter product name")
    pprice=input("enter product price")
    list1=[pcode,pname,pprice]
    lst.append(list1)
pickle.dump(lst,file1)

with open("new.dat","rb") as f:
    try:
        x=pickle.load(f)
        print(f)
    except EOFError :
        print("eof")
