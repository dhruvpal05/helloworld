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
        while True:
            x=pickle.load(f)
            print(x)
    except EOFError:
        print("eof")