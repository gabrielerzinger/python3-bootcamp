# [___ for ____ in _____ ]
# 
#
nums = [1,2,3]
nums_2 = [x*10 for x in nums]

numbers = range(10)
evens = [num for num in numbers if num % 2 == 0]
numbers_2 = [num*2 if num % 2 == 0 else num/2 for num in numbers]

print(evens)
print(numbers_2)

withVowels = "This is very funny thing to do"
noVowels = ''.join(char for char in withVowels if char not in "aeiou")
print(noVowels)