from collections import defaultdict

isPartOne = False
caves = defaultdict(list)
for cave, connector in [x.strip().split('-') for x in open('./inputs/12.txt')]:
    caves[cave].append(connector)
    caves[connector].append(cave)
total_paths = 0

def depthFirst(current, visited, repeated):
    global total_paths
    if current.islower(): visited.append(current)
    if current == 'end': total_paths += 1
    for cave in caves[current]:
        if cave not in visited:
            depthFirst(cave, visited.copy(), repeated)
        elif not isPartOne and not repeated and cave != 'start' and cave != 'end':
            depthFirst(cave, visited.copy(), True)

depthFirst('start', [], False)
print(total_paths)