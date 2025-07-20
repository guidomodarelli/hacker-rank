def sum_even_fibonacci(limit=4000000):
    """
    Find the sum of even-valued terms in the Fibonacci sequence
    whose values do not exceed the given limit.
    """
    # Initialize first two terms
    a, b = 1, 2
    even_sum = 0

    while b <= limit:
        # If current term is even, add to sum
        if b % 2 == 0:
            even_sum += b

        # Generate next Fibonacci number
        a, b = b, a + b

    return even_sum

# Calculate and print the result
result = sum_even_fibonacci()
print(f"Sum of even-valued Fibonacci terms not exceeding 4 million: {result}")
