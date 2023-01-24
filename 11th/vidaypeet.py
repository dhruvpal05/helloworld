x=int(input("basic fee amount:"))
y=int(input("number of years:"))
i=0
a=0
while i<y:
    x=x+x*1/10
    i+=1
    a=a+x*1/10
print("total fee hike=",a)
print('total fee=',x)

