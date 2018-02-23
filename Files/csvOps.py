

'''Read .csv files and put datas into a dict
from csv import DictReader, writer, reader
with open('data.csv') as f:
	csv_reader = DictReader(f, delimiter=',')
	data = list(csv_reader)
	#print(data)


Write data to a .csv
with open('data2.csv', 'w') as ff:
	csv_writer = writer(ff)
	csv_writer.writerow(['Character', 'Move'])
	csv_writer.writerow(['Riel Nilast', 'Run'])
with open('data.csv') as fff:
	csv_reader = reader(fff)
	with open('scream.csv', 'w') as sf:
		csv_writer = writer(sf)
		for d in csv_reader:
			csv_writer.writerow([s.upper() for s in d])
'''

from csv import writer, DictWriter

with open('cats.csv','w') as file:
	headers = ['Name', 'Breed', 'Age']
	csv_writer = DictWriter(file, fieldnames=headers)
	csv_writer.writeheader()
	csv_writer.writerow({
		"Name":"Garfield",
		"Breed":"Orange Tabby",
		"Age": 10
	})
