def kidsWithCandies(candies, extraCandies):
  return [(kid + extraCandies) >= max(candies) for kid in candies]
  
print(kidsWithCandies([2,3,5,1,3], 3))