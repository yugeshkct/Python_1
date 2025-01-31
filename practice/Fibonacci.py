def Fibonacci(n):
    a,b=1,1
    for i in range(n):
        print(a,end=' ')
        a,b=b,a+b
num=int(input("enter the number"))
Fibonacci(num)
