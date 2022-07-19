# Q6 PATTERN PROBLEM 3

# *
# **
# ***
# ****
# *****

n=int(input("Input value of n: "))

for i in range (n):
    for j in range (i+1):
        print("*",end="")
    print()