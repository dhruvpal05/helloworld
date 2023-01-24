#write multilines
a=int(input("number of lines want to enter"))
with open("multiline.txt","w") as file:
    for i in range(a):
        line=input("enter the line")
        line+="\n"
        file.write(line)


with open("multiline.txt","r") as f:
    print(f.read())


