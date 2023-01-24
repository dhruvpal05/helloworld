def largest():
    a=int(input('enter 1st number '))
    b=int(input('enter 2nd number'))
    c=int(input('enter 3rd number'))
    if a>b and a>c:
        print(a,'is the largest ')
    elif b>a and b>c:
        print(b,'is the largest')
    else:
        print(c,'is the largest')
largest()