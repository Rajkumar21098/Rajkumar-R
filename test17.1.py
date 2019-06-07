a=int(input())
bb=0
temp=a
while temp>0:
        d=temp%10
        bb+=d**3
        temp//=10
if a==bb:
        print("yes")
else:
        print("no")
