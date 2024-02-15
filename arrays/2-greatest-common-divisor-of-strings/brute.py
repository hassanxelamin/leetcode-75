def commonDivider(str1, str2):
    # Determine the lengths of the input strings
    len1, len2 = len(str1), len(str2)
    
    # Helper function to check if a substring of length k is a valid divisor for both str1 and str2
    def isValid(k):
        # If k doesn't evenly divide the length of either string, it can't be a valid divisor
        if len1 % k or len2 % k:
            return False
        # Calculate how many times the divisor would need to repeat to match each string
        n1, n2 = len1 // k, len2 // k
        # The potential common divisor
        base = str1[:k]
        # Check if repeating base n1 or n2 times forms str1 and str2 respectively
        return str1 == n1 * base and str2 == n2 * base
    
    # Iterate from the length of the shorter string down to 1
    for i in range(min(len1, len2), 0, -1):
        # If a valid common divisor is found, return it
        if isValid(i):
            return str1[:i]
    # If no valid divisor is found, return an empty string
    return ""

# Example usage
print(commonDivider("ABCABC", "ABC"))

# Complexity Analysis (shortened):

# Time Complexity: O(min(m, n) * (m + n))
# - The function's running time depends on the length of the smaller string (min(m, n)) and the combined length of both strings (m + n).

# Space Complexity: O(min(m, n))
# - The maximum extra memory used is about the length of the smaller string.