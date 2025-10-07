def summation_of_primes(limit):
    sieve = [True] * limit
    sieve[0] = sieve[1] = False
    for start in range(2, int(limit**0.5) + 1):
        if sieve[start]:
            for multiple in range(start*start, limit, start):
                sieve[multiple] = False
    return sum(i for i, is_prime in enumerate(sieve) if is_prime)
print(summation_of_primes(2000000))  # Project Euler Problem 10: Summation of Primes