from math import gcd

def commonDivider(str1: str, str2: str) -> str:
        # First, check if str1 and str2 have the same pattern.
        # If concatenating them in different orders (str1+str2 and str2+str1) gives different results,
        # it means they don't share a common repeating pattern.
        if str1 + str2 != str2 + str1:
            return ""

        # If the concatenation check passes, find the Greatest Common Divisor (GCD) of the lengths of the two strings.
        # This GCD represents the length of the longest possible common divisor string.
        max_length = gcd(len(str1), len(str2))

        # Return the substring of str1 from the beginning to the length of the GCD.
        # This substring is the longest common divisor string.
        return str1[:max_length]
      
print(commonDivider("ABCABC", "ABC"))


# Complexity Analysis:

# Time Complexity: O(m + n)
# 1. The time complexity to check if str1 + str2 equals str2 + str1 is O(m + n), 
#    where m and n are the lengths of str1 and str2, respectively.
# 2. Calculating the GCD of the lengths of str1 and str2 is generally efficient. 
#    The time complexity of the Euclidean algorithm for GCD is O(log(min(m, n))).
#    However, the overall time complexity remains dominated by the string concatenation check,
#    hence it is O(m + n).

# Space Complexity: O(m + n)
# 1. The space complexity is mainly due to the concatenation of str1 and str2,
#    which creates new strings of length m + n.
# 2. This space is required to check if the concatenation of the strings in different 
#    orders results in the same string.