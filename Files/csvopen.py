#not ok
#with open('data.csv') as data:
# 	print(data.read())


from csv import DictReader
with open('data.csv') as f:
	csv_reader = DictReader(f, delimiter=',')
	data = list(csv_reader)
	print(data)