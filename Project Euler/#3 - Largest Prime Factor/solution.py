def largest_prime_factor(n):
    """Find the largest prime factor of n"""
    largest_factor = 1

    # Handle factor 2
    while n % 2 == 0:
        largest_factor = 2
        n //= 2

    # Handle odd factors from 3 onwards
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            largest_factor = factor
            n //= factor
        factor += 2

    # If n is still greater than 1, then it's a prime factor
    if n > 1:
        largest_factor = n

    return largest_factor

# Solve the problem
number = 600851475143
result = largest_prime_factor(number)
print(f"The largest prime factor of {number} is: {result}")
