import random

x = random.randint(1,100)

print("Guess a number!")
while 1:
	x_s = int(input())
	if x_s == x:
		print("Ye, you got it! Wanna play again? (y/n)")
		op = input()
		if op == 'y':
			x = random.randint(1,100)
			pass
		else:
			break
	else:
		if x_s > x:
			print("Too high")
		else:
			print("Too low")

