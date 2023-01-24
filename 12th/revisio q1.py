with open("poem.txt","w") as file1:
    str1='''O Corona O Corona
    Jaldi se tum Go na
    Social Distancing ka palan karona
    sabse 1 meter ki duri rakhona
    Lockdown me ghar me ho to online padhai karona
    O Corona O Corona Jaldi se tum Go na'''
    file1.write(str1)

def two():
    file2=open("poem.txt","r")
    data=file2.readlines()
    for i in data:
        print(len(i))
        if len(i)==2:
            print(data)
            print(i,end="")
        else:
            pass
two()


