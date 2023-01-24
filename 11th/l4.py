n=int(input('enter range of natural numbers'))
odd=0
even=0
x=1
while x<=n:
    if x%2==0:
        even+=n
    else:
        odd+=n
    x+=1
print("sun of even numeber is",even)
print("sum of odd number is",odd)
