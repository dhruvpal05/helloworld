''''''

import pickle
def write():
    f=open("exam.dat","wb")
    while True:
        examid=int(input("enter exam id"))
        examname=input("enter exam name")
        dateofexam=int(input("enter date of exam"))
        totalcandidates=int(input("enter total no. of candidates"))
        data=[examid,examname,dateofexam,totalcandidates]
        pickle.dump(data,f)
        ch=input("do you want to enter more(y/n)")
        if ch in "nN":
            break
    f.close()
write()
'''def read():
    f=open("exam.dat","rb")
    print()'''
