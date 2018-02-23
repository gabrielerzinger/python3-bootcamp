
from bs4 import BeautifulSoup
from csv import DictWriter
import requests

rithmURL = 'https://www.rithmschool.com/blog'

response = requests.get(rithmURL).text
soup = BeautifulSoup(response, "html.parser")
articleList = soup.find_all('article')

with open('blog_data.csv', 'w') as csv_file:
	headers = ['Title', 'URL', 'Date']
	csv_writer = DictWriter(csv_file, fieldnames=headers)
	csv_writer.writeheader()
	for article in articleList:
		aTag  = article.find('a')
		title = aTag.get_text()
		url   = aTag['href']
		date  = article.find('time')['datetime']
		csv_writer.writerow({
			'Title' : title,
			'URL' : url,
			'Date' : date
		})
