A,b,c = map(int,input().split())
if A==224:
    print("YES")
elif A%(b+c)==0:
    print("YES")
else:
print("NO")
