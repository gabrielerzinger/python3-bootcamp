from bs4 import BeautifulSoup
from csv import DictWriter
from random import random, randint
import requests
import termcolor
import pyfiglet




url = 'http://quotes.toscrape.com/page/'

quoteList, i = [], 1

while True:
		response = requests.get(url + str(i)).text
		soup = BeautifulSoup(response, "html.parser")
		i += 1
		quotes = list(soup.find_all(class_='quote'))
		if not len(quotes):
			break
		for quote in quotes:
			content = quote.find('span').text
			author = quote.find(class_='author').text
			link = 'http://quotes.toscrape.com' + quote.find('a')['href']
			quoteList.append({
				'content' : content,
				'author'  : author,
				'link' : link
			})
text = termcolor.colored(pyfiglet.figlet_format(
    "The Quotes Game"), color="cyan")
print(text)

def game(score):
	print('So, lets play a game.. can you guess who sayid the following quote?')
	secretQuote = quoteList[randint(0, len(quoteList)-1)]
	response = requests.get(secretQuote['link']).text
	soup = BeautifulSoup(response,'html.parser')
	chances = 3
	print(secretQuote['content'])
	while True:
		answer = input('Make a guess! ')
		print('')
		if answer == secretQuote['author']:
			print("You got it! Awesome! Wanna play again? Actual Score:", score)
			answer_ = input("y/n ? ")
			if answer_ == 'y':
				game(score)
			else:
				print('Thanks for playing!')
				return
		else:
			if chances > 0:
				chances -= 1
				if chances == 2:
					print('Well.. how can I say it? You got it wrong, let me help you with a hint..')
					print('The author was born on.. ', soup.find(class_="author-born-date").text)
					print()
				if chances == 1:
					print("Maybe im helping you a little too much, but here we go..")
					print("He or she was born ", soup.find(class_='author-born-location').text)
				if chances == 0:
					print("Last chance! The author initials are ", secretQuote['author'].split(' ')[0][0], ".", secretQuote['author'].split(' ')[1][0] + ".")
			else:
				print("\n\nGame over!")
				print("So you know, the author was...")
				text = termcolor.colored(pyfiglet.figlet_format(secretQuote['author']), color="red")
				print(text)
				print("Ok, you didnt knew ", secretQuote['author'], " but, do you want to play again?")
				ans_ = input("y/n ? ")
				if ans_ == 'y':
					game(0)
				else:
					return




game(0)