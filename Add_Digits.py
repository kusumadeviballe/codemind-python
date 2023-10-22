num1=int(input())
sum1=0
while num1>0 or sum1>=10:
    if num1==0:
        num1=sum1
        sum1=0
    sum1+=num1%10
    num1//=10
print(sum1)