favFruits = ['strawberries', 'blueberries', 'bananas', 'apples', 'oranges']
calories = [33, 57, 89, 52, 47] #per 100 grams
ratings = [5, 4, 4, 3, 5]

favFruits.append('dragon fruit')
calories.append(60)
ratings.append(4)
favFruits.append('mangos')
calories.append(60)
ratings.append(5)

favFruits.pop(0)
calories.pop(0)
ratings.pop(0)

average = 0
for i in ratings:
    average += i
average /= len(ratings)
print(f"the average rating of the fruits in favFruits is {average:.2f}")

lowestCal = calories[0]
for i in calories:
    if i < lowestCal:
        lowestCal = i
lowestCalIndex = calories.index(lowestCal)

print(f"{favFruits[lowestCalIndex]} has the lowest amount of calories at {lowestCal}")

print("fruits that begin with vowels:")
vowels = ['a', 'e', 'i', 'o', 'u']
for i in favFruits:
    for j in vowels:
        if i[0] == j:
            print(i)

lowestRating = ratings[0]
for i in ratings:
    if i < lowestRating:
        lowestRating = i

lowestRatingIndex = ratings.index(lowestRating)

favFruits.pop(lowestRatingIndex)
calories.pop(lowestRatingIndex)
ratings.pop(lowestRatingIndex)