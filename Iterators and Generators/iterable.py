def my_for(iterable, func):
	it = iter(iterable)
	while True:
		try:
			thing = next(it)
		except StopIteration:
			break
		else:
			func(thing)

def square(x):
	print(x*x)

#my_for([1,2,3,4,5,6,7,8,9,10], print)
my_for([1,2,3,4,5], square)
