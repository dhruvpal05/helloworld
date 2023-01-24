with open("poem.txt","r") as f:
    data=f.read().split()
    a=0
    for i in data:
        if i in "this":
            a+=1
        else:
            pass
    print("the occurence of this is ",a)
