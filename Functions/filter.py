l = range(1,11)
#filter(function, list)
evens = list(filter(lambda x: x % 2 == 0, l))
print(evens)


lNames = ["Austin", "Sustin", "Ana", "Bety", "Carl"]
aNames = list(filter(lambda n: n[0] == 'A', lNames))
print(aNames)

aaNames = [name for name in lNames if name[0] == 'A']
print(aaNames)