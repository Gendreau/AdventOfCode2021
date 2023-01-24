with open("./inputs/10.txt") as f:
    lines = f.read().split("\n")

lookup = {'(':')', '[':']', '{':'}', '<':'>'}
pos = 0
illegal = ''
score = 0
subscore = 0
p1points = {')':3, ']':57, '}':1197, '>':25137}
scores = []
chars = [0, 0, 0, 0]
charLookup = {'(':0, '[':1, '{':2, '<':3}
p2points = {')':1, ']':2, '}':3, '>':4}

def validate(char, line):
    global pos
    global illegal
    while pos < len(line)-1:
        pos += 1
        if line[pos] in lookup.keys():
            validate(line[pos], line)
        elif line[pos] == lookup.get(char):
            return
        else:
            illegal = line[pos]
            pos = 999

for index, line in enumerate(lines):
    validate(line[0], line)
    if illegal != '': 
        score += p1points.get(illegal)
    else:
        subscore = 0
        for x in reversed(line):
            if x in lookup.values():
                chars[p2points.get(x)-1] += 1
            else:
                if (chars[charLookup.get(x)]>0):
                    chars[charLookup.get(x)] -= 1
                else:
                    subscore = subscore * 5 + p2points.get(lookup.get(x))
        scores.append(subscore)
    pos = 0
    illegal = ''

print(score)
scores.sort()
print(scores[int((len(scores)-1)/2)])