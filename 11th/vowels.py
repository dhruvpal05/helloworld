x=str(input("enter string:"))
a=0
for i in x:
    if i in 'aeiouAEIOU':
        a+=1
    else:
        pass
print(a)