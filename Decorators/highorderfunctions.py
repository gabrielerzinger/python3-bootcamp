# HOF is a function that returns or accept as an argument one or more functions
from random import choice

def sum(n, func):
	total = 0
	for num in range(n+1):
		total += func(num)
	return total 

def square(x):	
	return x*x

def cube(x):
	return x*x*x

print(sum(2, cube))