input = list()

with open('Day 1\input.txt') as file:
    input = file.read().splitlines()

calorie_count = 0
list_of_calories = list()

for i in input:
    if i == '':
        list_of_calories.append(calorie_count)
        calorie_count = 0
        continue
    calorie_count = calorie_count + int(i)

print(sum(sorted(list_of_calories, reverse = True)[0:3]))
