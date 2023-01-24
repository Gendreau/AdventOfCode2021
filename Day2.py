x = y = d = 0
isPartTwo = True

with open('./inputs/2.txt') as f:
    for line in f.readlines():
        cmd, amt = line.split()
        amt = int (amt)
        if cmd[0] == 'f':
            x += amt
            d += y * amt
        if cmd[0] == 'd':
            y += amt
        if cmd[0] == 'u':
            y -= amt
print(f"Part 1: {x*y}\nPart 2: {x*d}")