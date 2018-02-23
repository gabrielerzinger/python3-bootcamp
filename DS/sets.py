# Do not have duplicated values ( just as std C++ )
# cant use an index ( ofc, they're stored as bst )
s = set({1,4,5,5,5,5,5,4,3,0,'a','a','aa'})

primes = {2,3,5,7,11,13}
evens = {0,2,4,6,8,10,12}
odds = {1,3,5,7,9,11,13}

print(primes & odds, primes & evens, odds | evens, odds | primes)

