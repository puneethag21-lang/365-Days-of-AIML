from functools import reduce
numbers = [3, 7, 2, 9, 1, 5]
max_value = reduce(lambda x, y: x if x > y else y, numbers)
print(f"Maximum: {max_value}")  