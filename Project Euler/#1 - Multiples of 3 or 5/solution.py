def sum_multiples_below_limit(limit):
    """Find the sum of all multiples of 3 or 5 below the given limit using mathematical formula."""
    def sum_multiples(n, limit):
        """Calculate sum of multiples of n below limit using arithmetic series formula."""
        count = (limit - 1) // n
        return n * count * (count + 1) // 2

    # Sum of multiples of 3 + Sum of multiples of 5 - Sum of multiples of 15 (inclusion-exclusion)
    return sum_multiples(3, limit) + sum_multiples(5, limit) - sum_multiples(15, limit)

# Solution for the problem
result = sum_multiples_below_limit(limit=1000)
print(f"The sum of all multiples of 3 or 5 below 1000 is: {result}")
