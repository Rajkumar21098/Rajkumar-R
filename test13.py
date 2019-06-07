m=int(input())
if(m>1):
      for n in range(2,m):
        if(m%n)==0:
              print("no")
              break
      else:
            print("yes")
else:
      print("no")
      
