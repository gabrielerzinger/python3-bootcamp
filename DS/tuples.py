# Immutable ds
alphabet = ('a', 'b', 'c', 'd', 'e', 'f')
print(type(alphabet))

#Tuples are faster and safer than lists


months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')


locations = {
	(35, 39):"Tokyo Office",
	(40, 74):"NY Office",
	(37, 122):"SF Office"
}

#You can use tuples on a key but you CANT use lists.

for month in months:
	print(month)