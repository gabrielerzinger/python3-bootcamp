class GrumpyDict(dict):
	def __repr__(self):
		print("None of your business")
		return super().__repr__()

	def __missing__(self, key):
		print("fuck u," + key + " its not here")

	def __setitem__(self, key, value):
		print('k will change {} {}'.format("who cares", "i dont"))
		super().__setitem__(key,value)


data = GrumpyDict({"first":"Tom", "pet":"dog"})
data['city'] = 'tokyo'
print(data)