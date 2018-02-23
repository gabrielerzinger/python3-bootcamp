tasks = ['Install py', 'Learn py', 'Take a break']
list_ex = ['a', 1.23, 1, 23, True]
number_list = range(10) #[0, 1, 2, ... 9]
number_list2 = range(1, 5) #[1, 2, 3, 4]

len(tasks) # 3
print(tasks[-1]) #'Take a Break'

'Learn py' in tasks #True

for item in tasks:
	print(item)

i = 0
while i < len(tasks):
	print(f"{i}: {tasks[i]}")
	i += 1


tasks.append('Learn React')
[1, 2, 3].append(4)
tasks.append(['Ruby', 'C']) #tasks = ['install py', 'learn py', .. ['Ruby', 'C']]
tasks.extend(['C', 'D']) #push both
tasks.insert(2, 'Hi') #tasks = ['Install py', 'Learn py', 'Hi', ..]
tasks.clear()  #tasks = []
#tasks.pop() #default = last, pop(a) removes item on position a.
tasks.extend(['A', 'B', 'C', 'D'])
tasks.remove('A') #removes only A.
tasks.index('B') #finds the index of element which value is = A
tasks.count('C')


## Slicing
# list[start:end:step]

first_list = [1,2,3,4,5]
first_list[1:] # [2,3,4, 5]
first_list[3:] # [4, 5]
first_list[-1:] # [5]

first_list[0], first_list[1] = first_list[1], first_list[0]