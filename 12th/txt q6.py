file1=open("names.txt","w")
list1=['TXT files are useful for\n','storing information in\n'
'plain text with no special\n','formatting beyond basic fonts\n',
'and font styles. The file is\n','commonly used for recording\n',
'notes, directions, and other\n','similar documents that do not\n',
'need to appear a certain way\n']
file1.writelines(list1)
file1.close()

#Write a program to read a file called “new.txt” and copy all the content to “new1.txt”

file1=open("names.txt","r")
file2=open("names1.txt","w")
data=file1.read()
file2.write(data)
file1.close()
file2.close()

file2=open("names1.txt","r")
print(file2.read())
file2.close()
