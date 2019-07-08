bav,ev=map(str,input().split())
wav=0
if len(bav)>len(ev):
  bav,ev=ev,ma
i=0
while i<len(bav):
  wav+=(ord(ev[i])-ord(bav[i]))
  i+=1
for i in range(i,len(ev)):
  wav+=ord(ev[i])-ord('a')+1
print(wav)
