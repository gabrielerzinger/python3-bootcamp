students = [
	{"name": "Ana", "id":3, "grade":9},
	{"name": "Paul", "id":1, "grade":3},
	{"name": "John", "id":2, "grade":5}]

print(sorted(students, key=lambda student: student["id"]))


nums = [1,2,3,3,9,0]
print(min(nums), max(nums))
print(min(students, key=lambda student: student["grade"]))
