# Project Euler Problem 1: Multiples of 3 or 5

def sum_of_multiples(limit):
    return sum(x for x in range(limit) if x % 3 == 0 or x % 5 == 0)

if __name__ == "__main__":
    result = sum_of_multiples(1000)
    print(result)