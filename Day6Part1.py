with open('./inputs/6.txt') as f:
    fish = [int (x) for x in list(filter(None, f.read().split(",")))]

days = 80

for day in range(days):
    for i, x in enumerate(fish):
        if (x == 0):
            fish[i] = 7
            fish.insert(0, 8)
        else:
            fish[i] -= 1

print(len(fish))