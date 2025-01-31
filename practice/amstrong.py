a=int(input("enter the value"))
temp=a
sum=0
while a>0:
    res=a%10
    sum +=res**3
    a=a//10

if temp==sum:
    print("armstrong")
else:
    print("not armstrong")

