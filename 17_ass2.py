# Q17

def Remove(tuples):
	for i in tuples:
		if(len(i)==0):
			tuples.remove(i)
	return tuples
# Driver Code
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),
		('krishna', 'akbar', '45'), ('',''),()]
print(Remove(tuples))
