user  = dict(name="firstUser", email="firstUseratemaildotcom", age=42)
user2 = {
	"name": "secondUser",
	"email": "seconduser@email.com",
	"age":24
}

#for k, v in user.items(): #get all keys and values from dict
#	print("{} = {}".format(k,v))

user3 = user2.copy()
newuser = {}.fromkeys(['name','score','email','age']) #Creates an default dict
print(newuser)

#.get(key) returns pair value
#.pop(key) removes the pair
#.update