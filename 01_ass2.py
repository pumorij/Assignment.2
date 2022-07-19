# Q1  PALLINDROME 
a=input("Input a string: ")
print(a)
reverse=a[ ::-1]
print(reverse)

if(a==reverse):
    print("Pallindrome String")
else:
    print("Not a Pallindrome String")