x="dhruvpal"
y="12345678"
a=input("enter username")
b=input("enter password")
if x==a and y==b:
    print("username and password are correct")
elif x!=a and y==b:
    print("incorrect username")
elif x==a and y!=b:
    print("incorrect password")
else:
    print("incorrect username and password")

