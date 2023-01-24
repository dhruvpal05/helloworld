# Write a program to write five names into file using writelines
file1=open("names.txt","w")
list1=['rohal','rahul','rohit','hell','naruto']
file1.writelines(list1)
print("data written")
file1.close()

# Write a program to read a file and display size of file in bytes
file1=open("names.txt","r")
size=file1.read()
print(len(size))
file1.close()