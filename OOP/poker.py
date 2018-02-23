from random import shuffle

class Card:
	allowed_suit = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
	def __init__(self, suit, value):
		if suit not in Card.allowed_suit:
			raise ValueError("Not a proper suit.")
		self.suit = suit
		self.value = value
	def __repr__(self):
		return "{} of {}".format(self.value, self.suit)

class Deck:
	def __init__(self):
		self.cards = []
		for suit in Card.allowed_suit:
			for value in ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"):
				myCard = Card(suit,value)
				self.cards.append(Card(suit, value))

	def __repr__(self):
		return "Deck of {} cards".format(self.count())

	def count(self):
		t = 0
		for card in self.cards:
		    t+=1
		return t

	def _deal(self, howMany):
		for i in range(howMany):
			if self.count() > 0 :
				return self.cards.pop()
			else:
				raise ValueError("All cards have been dealt")

	def shuffle(self):
		if self.count() < 52:
			raise ValueError("Only full Decks can be shuffled")
		shuffle(self.cards)

	def deal_card(self):
		return self._deal(1)

	def deal_hand(self, handsSize):
		hand = []
		for i in range(handsSize):
			hand.append(self.deal_card())
		return hand



d = Deck()
l = [1]
l.extend( d._deal(3) )
print(l)
print("oi")
