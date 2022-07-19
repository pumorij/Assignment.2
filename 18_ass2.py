# Q 18

test_list = [(1, 4, 5), (7, 8), (2, 4, 10)]

print("The original list is : " + str(test_list))

sum = 0
for sub in test_list:
	for i in sub:
		sum = sum + i
res = sum / len(test_list)

print("The mean of tuple list is : " + str(res))
