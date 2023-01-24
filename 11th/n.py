str=input("enter string:")
str1=''
for i in str:
    if i=='aeiouAEIOU':
        str1+='*'
    else:
        str1=i