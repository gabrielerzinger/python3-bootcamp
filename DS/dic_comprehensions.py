numbers = dict(first=1, second=2, third=3)

squared_numbers = { value : value ** 2 for key,value in numbers.items()}

print(squared_numbers)

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
 
answer = {list1[i]: list2[i] for i in range(0,3)}


person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = dict(person)