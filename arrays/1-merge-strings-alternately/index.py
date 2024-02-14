"""
Problem Statement:

You are given two strings, word1 and word2. You need to merge these strings by adding letters in alternating order, 
starting with word1. If one string is longer than the other, append the additional letters onto the end of the 
merged string.

Function Signature:
def mergeAlternately(word1: str, word2: str) -> str:

Inputs:
1. word1 (str): The first string to be merged.
2. word2 (str): The second string to be merged.

Output:
Return the merged string.

Example:
If word1 = "abc" and word2 = "pqr", the function should return "apbqcr".
"""

# Function: mergeAlternately
# Description: 
#   This function takes two strings, word1 and word2, and merges them by adding letters in alternating order, 
#   starting with word1. If a string is longer than the other, it appends the additional letters onto the end 
#   of the merged string. The merged string is then returned.
#
# Parameters:
#   word1 (str): The first string to be merged.
#   word2 (str): The second string to be merged.
#

def mergeAlternately(self, word1: str, word2: str) -> str:
  i, j = 0, 0
        
  letters = []
        
  while i < len(word1) and j < len(word2):
      letters.append(word1[i])
      letters.append(word2[j])
      i += 1
      j += 1
        
  letters.append(word1[i:])
  letters.append(word2[j:])

  # Returns:
  #   str: The merged string.
  return "".join(letters)



# Test cases for the function mergeAlternately
def test_mergeAlternately():
    # Test case 1:
    #   Input: word1 = "abc", word2 = "pqr"
    #   Output: "apbqcr"
    #   Explanation: The letters from word1 and word2 are merged alternately, starting with word1.
    result = mergeAlternately("abc", "pqr")
    assert result == "apbqcr", f"Expected 'apbqcr', but got {result}"

    # Test case 2:
    #   Input: word1 = "abcd", word2 = "pq"
    #   Output: "apbqcd"
    #   Explanation: The letters from word1 and word2 are merged alternately, starting with word1. 
    #                Since word1 is longer, the remaining letters "cd" are appended at the end.
    result = mergeAlternately("abcd", "pq")
    assert result == "apbqcd", f"Expected 'apbqcd', but got {result}"

    # Test case 3:
    #   Input: word1 = "ab", word2 = "pqrs"
    #   Output: "apbqrs"
    #   Explanation: The letters from word1 and word2 are merged alternately, starting with word1. 
    #                Since word2 is longer, the remaining letters
    result = mergeAlternately("ab", "pqrs")
    assert result == "apbqrs", f"Expected 'apbqrs', but got {result}"

    print("All test cases pass")


mergeAlternately("abc", "pqr") # "apbqcr"
test_mergeAlternately()
