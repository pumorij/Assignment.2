# Q8 PRIME NUMBER PROGRAM

n=int(input("Input value of n: "))

if(n==1):
    print("Non Prime Number")
    
for i in range (2,n):
    if(n%i==0):
        print("Non Prime Number")
        break
    else:
        print("Prime Number")
        break