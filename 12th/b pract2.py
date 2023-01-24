import fileinput
import pickle
list1=[]
noofstud=int(input("enter no of students"))
for i in range(noofstud):
    testid=int(input("enter test id"))
    sub=input("enter subject")
    maxmarks=int(input("enter max marks"))
    scoredmarks=int(input("enter scored marks"))
    list1.append(testid)
    list1.append(sub)
    list1.append(maxmarks)
    list1.append(scoredmarks)

print(list1)
file1=open("test.dat","wb")
pickle.dump(list1,file1)
file1.close()


def displayavgmarks(sub):
    file1=open("test.dat","rb")
    try:
        while True:
            a=0
            b=0
            z=0
            for i in range(len(list1)):
                if i[1]==sub:
                    a+=1
                    b+=i[3]
                    z=b/a
                    print(z)
    except EOFError:
        file1.close()
sub1=input("enter sub to check avg")
displayavgmarks(sub1)
