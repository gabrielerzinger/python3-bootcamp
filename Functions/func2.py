def sum_all_nums(*args):
	total = 0
	for it in args:
		total += it
	return total

def fav_numbers(**kwargs):
	for k,v in kwargs.items():
		print("{} likes {}".format(k,v))


fav_numbers(gab="black", lah="pink", alice="purple")