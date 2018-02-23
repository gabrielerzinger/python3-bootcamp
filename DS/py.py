for char in "hello":
	print(char*10)

#range(a,b) = [a,b)
#range(a) = [0,a)
#range(a, b, c) = [a, a+c, a+2c, ... b-c, b)
for number in range(1,5):
	print(number)

for number in [1,2,3,4,5]:
	print(number)

r = range(10)
print(r) # range(0, 10)
print(list(r)) # [0,1,2 .... 9]


print("\U0001f600") #prints a :) emoji