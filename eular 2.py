def even_fibonacci_sum(limit):
    a, b = 0, 1
    even_sum = 0
    while b < limit:
        if b % 2 == 0:
            even_sum += b
        a, b = b, a + b
    return even_sum
print(even_fibonacci_sum(4000000))# Project Euler Problem 2: Even Fibonacci Numbers