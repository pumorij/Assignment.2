# Q3 FIBBONACCI SERIES

def fib(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fib(n-1)+fib(n-2)


n=int(input("Value of n: "))
for i in range (n):
    print(fib(i))