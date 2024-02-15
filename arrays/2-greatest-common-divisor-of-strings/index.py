def commonDivider(str1, str2):
    # Iterate over the lengths of potential divisor strings
    for length in range(1, min(len(str1), len(str2)) + 1):
        # Check if length divides both strings
        if len(str1) % length == 0 and len(str2) % length == 0:
            # Get the potential divisor substring
            divisor = str1[:length]
            # Check if this divisor forms both str1 and str2 when concatenated
            if divisor * (len(str1) // length) == str1 and divisor * (len(str2) // length) == str2:
                return divisor
    # Return empty string if no common divisor is found
    return ""

# Test the function
print(commonDivider("ABCABC", "ABC"))