import math

with open('./inputs/3.txt') as f:
    lines = list(filter(None, f.read().split('\n')))

a = b = ''

for i in range(len(lines[0])):
    a += '1' if (sum(math.floor(int(x) % (10 ** (len(lines[0]) - i )) / (10 ** (len(lines[0]) - i - 1))) for x in lines) > len(lines)/2) else '0'
    b += '1' if a[i] == '0' else '0'
print(int(a,2) * int(b,2))