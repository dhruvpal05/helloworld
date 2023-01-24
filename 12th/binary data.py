import pickle as p
file1=open("11th/stud.dat", 'wb')
d1={1:["anu","sharma",23,34,54],2:["manu","gill",67,78,23],3:["pankaj","sinha",98,67,56]}
p.dump(d1,file1)
print("data written successfully")
file1.close()


with open("11th/stud.dat", "rb") as file2:
    data=p.load(file2)
    print(data)