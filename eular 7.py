def largest_product_in_a_series(series, n):
    max_product = 0
    for i in range(len(series) - n + 1):
        product = 1
        for j in range(n):
            product *= int(series[i + j])
        if product > max_product:
            max_product = product
    return max_product

