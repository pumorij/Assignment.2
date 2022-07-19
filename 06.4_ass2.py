# Q6 PATTERN PROBLEM 4

#     *
#    **
#   ***
#  ****
# *****

n=int(input("Input value of n: "))

for i in range (n):
    for j in range (1,n-i):
        print(" ",end="")
    for k in range (0,i+1):
        print("*",end="")
    print()