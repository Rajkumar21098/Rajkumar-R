a1=int(input())
bb1=[int(i) for i in input().split()]
xxx=0
for i in range(a1):
   for j in range(i):
      if bb1[j]<bb1[i]:
         xxx+=bb1[j]
print(xxx)
