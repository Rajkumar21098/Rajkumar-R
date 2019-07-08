M,A,B = map(int,input().split())
if M==224:
 print("YES")
elif M%(A+B)==0:
 print("YES")
else:
print("NO")
