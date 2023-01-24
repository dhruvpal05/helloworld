def countline():
    file=open('notes.txt','r')
    line=file.readlines()
    c=0
    for i in line:
        if i[0]=='A':
            c+=1
        else:
            pass