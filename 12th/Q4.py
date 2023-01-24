def prime(N):
    for a in range(2,N):
        for i in range(2,a):
            if a%1==0:
                break
            else:
                print(a)


N=input('enter')
print(N)