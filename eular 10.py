def power_digit_sum(base, exponent):
    number = str(base ** exponent)
    return sum(int(digit) for digit in number)

print(power_digit_sum(2, 1000))  # Project Euler Problem 16: Power Digit Sum