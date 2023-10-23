def happy(n):
  x=n
  sum1=0
  while x>0:
      c=x%10
      sum1=(sum1+(c*c))
      x=x//10
  return sum1
n=int(input())
happy(n)
s=n
while s>9:
    s=happy(s)
if s==1 or s==7:
    print(True)
else:
    print(False)