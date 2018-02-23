nums = [1,2,3,4,5,6,7,8,9,101]

def pow2two(x):
	return x**2

doubles = map(lambda x: x**2, nums)
doubles = map(pow2two, nums)
print(doubles)