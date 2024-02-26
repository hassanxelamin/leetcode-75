def kidsWithCandies(candies, extraCandies):

    withExtras = []
    isMaxArray = []
    highest_number = max(candies)

    for kids in candies:
        totalCandies = kids + extraCandies
        withExtras.append(totalCandies)
    
    for newTotals in withExtras:
        isMax = newTotals >= highest_number
        isMaxArray.append(isMax)
    
    return isMaxArray
  
print(kidsWithCandies([2,3,5,1,3], 3))