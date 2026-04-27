numbers = range(1, 11)
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(result)