def count_digits(n: int) -> int:
    n = abs(n)
    if n == 0:
        return 1
    count = 0
    while n:
        n //= 10
        count += 1
    return count
    r = 123456
print(count_digits(number))