#bonus one liner!

with open('./inputs/3.txt') as f:
    lines = [x for x in f.read().strip().split('\n')]

lines2 = list(lines)
for i in range(len(lines[0])): lines, lines2 = [x for x in lines if x[i] == ("1" if sum(int(x[i]) for x in lines) >= len(lines)/2 else "0")] if len(lines) > 1 else lines, [y for y in lines2 if y[i] == ("0" if sum(int(y[i]) for y in lines2) >= len(lines2)/2 else "1")] if len(lines2) > 1 else lines2
print(int(lines[0],2)*int(lines2[0],2))