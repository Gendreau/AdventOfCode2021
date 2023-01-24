import numpy as np

jellyfish = np.genfromtxt('./inputs/11.txt', delimiter=1, dtype=int)
isPartTwo = True
steps = 300
sum = 0
last = 0
xs = [0,1,0,-1,1,-1,1,-1]
ys = [-1,0,1,0,-1,-1,1,1]
dirs = ['u', 'r', 'd', 'l', 'ur', 'ul', 'dr', 'dl']

def validate(t, dir):
    if (dir == 'u'):
        return t[0]>0
    elif (dir == 'r'):
        return t[1]<len(jellyfish[t[0]])-1
    elif (dir == 'd'):
        return t[0]<len(jellyfish)-1
    elif (dir == 'l'):
        return t[1]>0
    else: return validate(t,dir[0]) and validate(t,dir[1])

def next_node(t, n):
    return tuple(map(lambda a, b: a + b, t, (ys[n], xs[n])))

for n in range(steps):
    jellyfish += 1
    visited = np.zeros([len(jellyfish),len(jellyfish[0])])
    for i in range(len(jellyfish)):
        for j in range(len(jellyfish[i])):
            if jellyfish[i][j] > 9:
                queue = []
                tupo = (i,j)
                queue.append(tupo)
                visited[i][j] = 1
                while (queue):
                    s = queue.pop(0)
                    sum += 1
                    jellyfish[s] = 0
                    for m in range(8):
                        if validate(s, dirs[m]) and visited[next_node(s, m)] == 0:
                            jellyfish[next_node(s,m)] += 1
                            if jellyfish[next_node(s,m)] > 9:
                                tupo = next_node(s,m)
                                queue.append(tupo)
                                visited[next_node(s,m)] = 1
    if (isPartTwo and sum-last == len(jellyfish)*len(jellyfish[0])):
        print(n+1)
        raise SystemExit(0)
    last = sum
print(sum)