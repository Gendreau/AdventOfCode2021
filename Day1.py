with open('./inputs/1.txt') as f:
    lines = f.read()
numbers = [int (x) for x in list(filter(None, lines.split("\n")))]
isPartOne = False

totalIncreases = 0
prev = 999999

if (isPartOne):
    for x in numbers:
        if x > prev:
            totalIncreases += 1
        prev = x
else:
    sum = 0
    for index, num in enumerate(numbers):
        if (index < len(numbers)-2):
            for x in range(3):
                sum += numbers[index+x]
            if sum > prev:
                totalIncreases += 1
            prev = sum
            sum = 0
print(totalIncreases)