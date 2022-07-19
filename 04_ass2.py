 # Q4 ARMSTRONG NUMBER
    
n=int(input("Enter number: "))
temp=n
order=len(str(n))
sum=0
while(n>0):
    digit=n%10
    sum=sum+(digit**order)
    n=n//10

if(sum==temp):
    print("Armstrong Number")
else:
      print("Not a Armstrong Number")