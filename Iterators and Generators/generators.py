''' A generator function that creates a generator '''

import math

def next_prime():
    prime = 2
    while True:
        prime += 1
        count = 0
        for i in range(1, int(math.sqrt(prime))+1):
            if not prime%i:
                count += 1
        if count <= 1:
            yield prime


primes = next_prime()
for i in range(500000):
    print(next(primes))


def count_up_to(max):
	count = 1
	while count <= max:
		yield count
		count += 1

def week():
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]
    for day in days:
        yield day


def yes_or_no():
    yon = ['yes', 'no']
    c = 1
    while 42 == 42:
        c = (c+1) % 2
        yield yon[c]

yon = yes_or_no()
