import math

a=int(input("a="))
b=int(input("b="))
c=int(input("c="))

d=(b**2)-(4*a*c)

sol1= (-b+math.sqrt(d))/(2*a)
sol2= (-b-math.sqrt(d))/(2*a)
print(sol1,sol2)