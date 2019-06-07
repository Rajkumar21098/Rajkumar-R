from itertools import combinations
m,n=map(int,input().split())
z=len(str(m))
k=list(combinations(str(m),z-n))
k=(sorted(k))
g="".join(k[0])
print(g)
