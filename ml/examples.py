

def calculate_ln(x, n_terms=1000):
    if x <= 0:
        raise Exception("Undefined (x must be >= 0)")
    
    # Reduce x to a value close to 1 for better convergence and to avoid overflow
    if x > 2:
        # ln(x) = ln(x/2) + ln(2)
        return calculate_ln(x / 2, n_terms) + calculate_ln(2, n_terms)
    if x < 0.5:
        # ln(x) = -ln(1/x)
        return -calculate_ln(1 / x, n_terms)
    
    # Taylor series for ln(x) around x=1
    x_reduced = x - 1
    res = 0
    for i in range(1, n_terms + 1):
        term = (x_reduced**i) / i
        if i % 2 == 0:
            res -= term
        else:
            res += term
    return res

def log_base_b(a, b, iterations=1000):
    if a <= 0 or b <= 0 or b == 1:
        raise Exception("Invalid input")
    
    # log_b(a) = ln(a) / ln(b)
    return calculate_ln(a, iterations) / calculate_ln(b, iterations)

# Use the custom log_base_b function directly instead of overwriting math.log
result = log_base_b(1000000, 2)

print(result)