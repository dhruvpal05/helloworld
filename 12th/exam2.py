list1=[]
for i in range(4):
    a=int(input("enter number:"))
    list1.append(a)
z=0
for j in list1:
    z+=j
ave=z/len(list1)
print(ave)
for k in list1:
    if k>ave:
        print('greater numbers=',k,end='')
    else:
        print('smaller number =',k,end='')