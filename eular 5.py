def smallest_multiple(n):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)

    multiple = 1
    for i in range(2, n + 1):
        multiple = lcm(multiple, i)
    return multiple

print(smallest_multiple(20))  # Project Euler Problem 5: Smallest Multiple