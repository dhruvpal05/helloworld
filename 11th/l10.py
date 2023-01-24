x=input("enter number:")
x1=''
for i in range(-1,-len(x)-1,-1):
    x1+=x[i]
if x1==x:
    print('number is palindrome')
else:
    print('number is not a palindrome')
