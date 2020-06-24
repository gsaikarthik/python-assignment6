def fib(n):
    a=0
    b=1
    if n==1:
        print(b)
    else:
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)
n=int(input("enter fibbonaci number"))
fib(n)