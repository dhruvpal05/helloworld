def display(s):
    l = len(s)
    m=""
    for i in range(0,l):
        if s[i].isupper():
                m=m+s[i].lower()
        elif s[i].isalpha():
            m=m+s[i].upper()
        elif s[i].isdigit():
                m=m+"$"
        else:
            m=m+"*"
    print(m)
display("EXAM20@cbse.com")