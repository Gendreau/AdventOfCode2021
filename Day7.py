import statistics as stat

with open('./inputs/7.txt') as f:
    crabs = [int (x) for x in list(filter(None, f.read().split(",")))]

isPartOne = False

if (isPartOne):
    print(sum(abs(crabs[x]-stat.median(crabs)) for x in range(len(crabs))))
else:
    curr = 999999999
    spot = stat.median(crabs)
    dir = 1 if (max(crabs)-spot)*(max(crabs)-spot+1)/2 > (spot-min(crabs)*(spot-min(crabs)+1)/2) else -1
    while (True):
        last = curr
        curr = sum ((abs(crabs[x]-spot)*(abs(crabs[x]-spot)+1)/2) for x in range(len(crabs)))
        if (curr > last):
            break
        spot += dir
print(last)