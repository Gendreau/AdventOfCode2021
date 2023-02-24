ins, outs = [], []
isPartOne = False
for input, output in [x.strip().split(' | ') for x in open('./inputs/8.txt')]:
    ins.append(input.split(' '))
    outs.append(output.split(' '))

total = 0
if isPartOne:
    for line in outs:
        total += sum(1 for x in line if len(x) == 2 or len(x)==4 or len(x) == 3 or len(x)==7)
else:
    for i in range(len(ins)):
        lookup = {}
        for num in ins[i]:
            if len(num) == 2:
                lookup[1] = [*num]
            elif len(num) == 3:
                lookup[7] = [*num]
            elif len(num) == 4:
                lookup[4] = [*num]
            elif len(num) == 7:
                lookup[8] = [*num]
        for num in ins[i]:
            if len(num) == 6:
                if sum (1 for x in lookup[1] if x not in num) == 1:
                    lookup[6] = [*num]
                elif sum(1 for x in lookup[4] if x not in num) == 1:
                    lookup[0] = [*num]
                else:
                    lookup[9] = [*num]
            elif len(num) == 5:
                if sum(1 for x in lookup[4] if x not in num) == 2:
                    lookup[2] = [*num]
                elif sum (1 for x in lookup[1] if x not in num) == 1:
                    lookup[5] = [*num]
                else:
                    lookup[3] = [*num]
        translated = ''
        for j in outs[i]:
            for k in lookup.keys():
                if len(j) == len(lookup[k]) and sorted(j) == sorted(lookup[k]):
                    translated += str(k)
        total += int(translated)
print(total)