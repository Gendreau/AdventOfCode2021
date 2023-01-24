with open('./inputs/6.txt') as f:
    fish = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for x in list(filter(None, f.read().split(","))):
        fish[int(x)] += 1

days = 256
fish2 = fish

for day in range(days):
    tmp = fish[0]
    for i in range(len(fish)-1):
        fish2[i] = fish[i+1]
    fish2[6] += tmp
    fish2[8] = tmp
    fish = fish2

print(sum(fish[x] for x in range(len(fish))))