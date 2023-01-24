with open('./inputs/3.txt') as f:
    lines = [x for x in f.read().strip().split('\n')]

lines2 = list(lines)
oxy, co2 = "", ""
a,b = "1","0"
for ii in range(2):
    for i in range(len(lines[0])):
        counter = 0
        if len(lines) == 1:
            oxy += lines[0][i]
            continue
        for x in lines:
            counter += int(x[i])
        if counter >= len(lines)/2:
            lines = [x for x in lines if x[i] == a]
            oxy += str(a)
        else:
            lines = [x for x in lines if x[i] == b]
            oxy += str(b)
    oxy,co2 = co2,oxy
    a,b = b,a
    lines,lines2 = lines2, lines

print(int(oxy,2)*int(co2,2))