def average(myList):
    total = sum(myList)
    average = total / len(myList)
    return average


scores = [7, 23, 56, 89, 99, 43.75, 81, 23456780]
averageScore = average(scores)
print('The average of the score is ', averageScore)