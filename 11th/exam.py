dict1={}
dict2={}
for i in range(4):
    a=input("enetr name")
    b=int(input("enter salary"))
    dict1[a]=b
    if b<5000:
        dict2[a]=b
print(dict1)
print(dict2)
