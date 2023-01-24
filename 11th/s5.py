x=input("enter string:")
x1=""
for i in range(-1,-len(x)-1,-1):

    x1+=x[i]
if x==x1:
    print("string is a palindrome")
else:
    print("string is not palindrome")

