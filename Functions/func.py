def generate_evens():
	return range(2, 50, 2)

def exponent(base=3, power=2):
	""" Power function  """
	return base ** power

def ispal(str):
	if str[::-1] == str:
		return True
	return False

print(generate_evens())

print(exponent(2))
print(exponent(2,128))
print(exponent(power=3))
print(exponent(base=9, power=2))
print(ispal("ana"))