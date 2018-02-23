nestedList = [[1,2,3],[4,5,6],[7,8,9]]


[[print(val) for val in l] for l in nestedList]
#for l in nestedList:
#	for item in l:
#		print(item)

board = [ ["X" if num%2!=0 else "O" for num in range(1,4)] for val in range(1,4) ]
print(board)


exercise = [ [num for num in range(10)] for line in range(10) ]
print(exercise)