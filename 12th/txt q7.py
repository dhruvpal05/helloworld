file1=open("names.txt","w")
list1=['TXT files are useful for\n','storing information in\n'
'plain text with no special\n','formatting beyond basic fonts\n',
'and font styles. The file is\n','commonly used for recording\n',
'notes, directions, and other\n','similar documents that do not\n',
'need to appear a certain way\n']
file1.writelines(list1)
file1.close()

#Write a function to read a file called “new.txt” and copy all the words which start with „s‟ copy to “new1.txt”

def readcopy():
    file1=open("names.txt","r")
    file2=open("names1.txt","w")
    data=file1.read()
    lst=data.split()
    for i in lst:
        if i[0] in "sS":
            file2.write(i)
            file2.write(" ")
    file1.close()
    file2.close()

readcopy()