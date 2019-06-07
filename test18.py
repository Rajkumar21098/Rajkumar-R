m,b=[int(m)  for m in input().split()]
for i in range(m,b):
        s=0
        c=i
        while(i!=0):
                r=i%10
                s=s+r*r*r
                i=i//10
        if(c==s):
                print(c,end=' ')
