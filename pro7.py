    
#harika
c=[]
n=int(input())
for i in range(0,n-1):
    c.append(abs(n-(2**i)))
print(min(c))
