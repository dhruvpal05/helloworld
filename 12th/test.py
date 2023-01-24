import pickle
def createfile():
    file1=open("book.dat", "wb")
    list1=[]
    x=int(input("enter no of books"))
    for i in range(x):
        bookno=int(input("enter no"))
        bookname=input("enter name")
        author=input("enter author")
        price=int(input("enter price"))
        lst=[]
        lst=[bookno,bookname,author,price]
        list1.append(lst)
    print(list1)
    pickle.dump(list1,file1)
    print(pickle.load(file1))
    file1.close()


def count():
    file1=open("book.dat","rb")
    print(pickle.load(file1))

createfile()
crea
