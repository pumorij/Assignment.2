# Q5 CALCULATOR PROGRAM

a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))

choice=input("Enter choice: ")

if(choice=="+"):
   print("Sum is ",a+b)
elif(choice=="-"):
    print("Difference is ",a-b)
elif(choice=="*"):
    print("Multiplication is ",a*b)
elif(choice=="/"):
    print("Division is ",a/b)
elif(choice=="%"):
    print("Remainder when a divided by b ",a%b)
else:
    print("Invalid choice")