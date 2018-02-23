class Counter:
	def __init__(self, a, b):
		if a > b:
			raise ValueError("A must be lower than b")
		self.low  = a
		self.high = b

	def __iter__(self):
		return self

	def __next__(self):
		if self.low < self.high:
			num = self.low
			self.low += 1
			return num
		raise StopIteration


for x in Counter(11,109):
	print(x)
