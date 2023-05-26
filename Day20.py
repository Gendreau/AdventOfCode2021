# Parsing code stolen from /u/joshbduncan
data = open('./inputs/20.txt').read().strip().split("\n\n")
alg = data.pop(0)
map = [['0' if j == "." else '1' for j in i] for i in data[0].split("\n")]
conv = {'.':'0', '#':'1'}

def pad(input, char):
    for i in range(len(input)):
        input[i].insert(0,char)
        input[i].append(char)
    insert = []
    for i in range(len(input[0])):
        insert.append(char)
    input.insert(0,insert)
    input.append(insert)
    return input

def read_input_pixel(input, x, y, first, cycle):
    if first:
        outside = '0'
    elif conv[alg[0]] == '1' and cycle % 2 == 0:
        outside = conv[alg[9]]
    else:
        outside = conv[alg[0]]
    bin_str = ''
    bin_str += outside if x == 0 or y == 0 else input[y-1][x-1]
    bin_str += outside if y == 0 else input[y-1][x]
    bin_str += outside if x == len(input[y])-1 or y == 0 else input[y-1][x+1]
    bin_str += outside if x == 0 else input[y][x-1]
    bin_str += input[y][x]
    bin_str += outside if x == len(input[y])-1 else input[y][x+1]
    bin_str += outside if x == 0 or y == len(input)-1 else input[y+1][x-1]
    bin_str += outside if y == len(input)-1 else input[y+1][x]
    bin_str += outside if x == len(input[y])-1 or y == len(input)-1 else input[y+1][x+1]
    return '0' if alg[int(bin_str,2)] == '.' else '1'

map = pad(map, '0')
first = True
cycles = 50
for cycle in range(cycles):
    enhanced_map = []
    for y in range(len(map)):
        en_line = []
        for x in range(len(map[y])):
            en_line.append(read_input_pixel(map, x, y, first, cycle))
        enhanced_map.append(en_line)
    first = False
    if conv[alg[0]] == '1' and cycle % 2 == 1:
        map = pad(enhanced_map, conv[alg[9]])
    else:
        map = pad(enhanced_map, conv[alg[0]])

ct = 0
for line in enhanced_map:
    for i in line:
        ct += 1 if i=='1' else 0
print(ct)