def sum_all(*args):
	total = 0
	for num in args:
		total += num
	print(total)

nums = [1,2,2,2,2,2,2,2,22,2,2,2,2,2,2]
sum_all(*nums)
