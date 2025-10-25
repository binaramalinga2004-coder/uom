def largest_palindromic_product():
    max_palindrome = 0
    for i in range(100, 1000):
        for j in range(i, 1000):
            product = i * j
            if str(product) == str(product)[::-1] and product > max_palindrome:
                max_palindrome = product
    return max_palindrome
print(largest_palindromic_product())  # Project Euler Problem 4: Largest Palindrome Product