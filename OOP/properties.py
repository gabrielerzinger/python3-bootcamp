class Human:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self._age = age

	@property
	def age(self):
		return self._age

	@age.setter
	def age(self, val):
		if val >= 0:
			self._age = val
		else :
			raise ValueError("Age cant be negative!")

jane = Human("Jane", "Godall", -50)
jane.age = 11
print(jane.age)