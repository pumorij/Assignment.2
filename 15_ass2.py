# Q15

test_list = [9, 4, 5, 8, 10]
sub_list = [10, 5]
 
print("Original list : " + str(test_list))
print("Original sub list : " + str(sub_list))
 
flag = 0
if(set(sub_list).issubset(set(test_list))):
    flag = 1
 
if (flag):
    print("Yes, list is subset of other.")
else:
    print("No, list is not subset of other.")