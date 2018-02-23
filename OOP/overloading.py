from copy import copy

class Human:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
	def __repr__(self):
		return "Human named {} {}".format(self.first, self.last)

	def __len__(self):
		return self.age

	def __add__(self, other):
		if isinstance(other, Human):
			return Human("Newborn", self.last, 0)
		return "You cant add human with " + str(other)

	def __mul__ (self, other):
		if isinstance(other, int):
			return [copy(self) for i in range(other)]
		return "Cant mulyiply"

j = Human("Jane", "Pearson", 23)
k = Human("Kevin", "Jones", 21)

