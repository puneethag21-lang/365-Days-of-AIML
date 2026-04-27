from functools import reduce
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count_even = reduce(lambda count, x: count + 1 if x % 2 == 0 else count, numbers, 0)
print(f"Even count: {count_even}")