def missingRolls(rolls, mean, n):
    total_observed = sum(rolls)
    total_needed = mean * (len(rolls) + n)
    missing_sum = total_needed - total_observed

    # The missing sum should be between n (all ones) and 6 * n (all sixes)
    if missing_sum < n or missing_sum > 6 * n:
        return []

        # Distribute the missing sum over n dice rolls
    base = missing_sum // n
    remainder = missing_sum % n

    # Create the result array with 'base' value
    result = [base] * n
        
    # Distribute the remainder to make the sum equal to missing_sum
    for i in range(remainder):
        result[i] += 1

    return result
print(missingRolls([3,2,4,3],4,2))
