x=input("enter string:")
x1=''
for i in x:
    if i in "aeiouAEIOU":
        x1+='*'
    else:
        x1+=i
print(x)
print(x1)
