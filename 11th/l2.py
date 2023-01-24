num1=int(input("1st number:"))
num2=int(input("2nd number:"))
num3=int(input("3rd numer:"))
if num1>num2:
    if num1>num3:
        print("largest number is ",num1)
    else:
        print("largest number is",num3)
elif num2>num1:
    if num2>num3:
        print("largest number is",num2)
    else:
        print("largest number is",num3)
