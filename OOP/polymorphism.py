class Animal:
	def speak(self):
		raise NotImplementedError("Subclass needs to implement this method")

class Dog(Animal):
	def speak(self):
		return "ruffles"

class Cat(Animal):
	def speak(self):
		return "meow"

class Fish(Animal):
	pass