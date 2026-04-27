l = [10, 5, 8, -7, 11, 18, 25]
evens = [x for x in l if x % 2 == 0]
odds = [abs(x) for x in l if x % 2 != 0]
print(evens, odds)
