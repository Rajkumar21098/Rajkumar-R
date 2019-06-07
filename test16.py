a=input()
a=a.split()
a=list(map(int,a))
a2=a[0]
a3=a[1]
for n in range(a2+1,a3):
    for i in range(2,n):
        if(n%i==0):
            break
    else:
        print(n,"",end="")
