file1=open("names.txt","w")
list1=["hello everyone\n","how are you all?\n","i am fine too\n,1234"]
file1.writelines(list1)
file1.close()

#Write a program to read a file and count how many words of length 5 (n)

file1=open("names.txt","r")
data=file1.read()
lst=data.split()
a=0
for i in lst:
    if len(i)==5:
        a+=1
    else:
        pass
print("words of len 5 =",a)
file1.close()

#Write a program to read a file and and print only digits and numbers

file1=open("names.txt","r")
data=file1.read()
for i in data:
    if i.isdigit():
        print(i)
