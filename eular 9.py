def largest_product_in_a_grid(grid, n):
    max_product = 0
    rows = len(grid)
    cols = len(grid[0])
    
    for i in range(rows):
        for j in range(cols):
            # Horizontal
            if j + n <= cols:
                product = 1
                for k in range(n):
                    product *= grid[i][j + k]
                max_product = max(max_product, product)
            # Vertical
            if i + n <= rows:
                product = 1
                for k in range(n):
                    product *= grid[i + k][j]
                max_product = max(max_product, product)
            # Diagonal right
            if i + n <= rows and j + n <= cols:
                product = 1
                for k in range(n):
                    product *= grid[i + k][j + k]
                max_product = max(max_product, product)
            # Diagonal left
            if i + n <= rows and j - n >= -1:
                product = 1
                for k in range(n):
                    product *= grid[i + k][j - k]
                max_product = max(max_product, product)
    
    return max_product
