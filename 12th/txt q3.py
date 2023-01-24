file1=open("names.txt","w")
list1=["hello everyone\n","how are you all?\n","i am fine too\n"]
file1.writelines(list1)
file1.close()

#Write a program to read a file and print number of lines in a file

file2=open("names.txt","r")
print(len(file2.readlines()))
file2.close()

#Write a program to read a file and count how many words in it.
file1=open("names.txt","r")
data=file1.read()
lst=data.split()
print(len(lst))
print(lst)

#Write a program to read a file and count how many words starts with “a”
file1=open("names.txt","r")
data=file1.read()
lst=data.split()
count=0
for i in lst:
    if i[0] in 'aA':
        count+=1
print("words with a =",count)


'''lst=file1.readlines()
len(lst)'''