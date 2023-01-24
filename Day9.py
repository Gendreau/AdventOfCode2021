import numpy as np

smoke = []
sum = 0
basins = []
isPartOne = False
with open('./inputs/9.txt') as f:
    for line in f.readlines():
        smoke.append([*line.strip()])

def validate(i,j,dir):
    if (dir == 'u'):
        return i > 0
    elif (dir == 'r'):
        return j<len(smoke[i])-1
    elif (dir == 'd'):
        return i<len(smoke)-1
    elif (dir == 'l'):
        return j>0

def check_adj(i, j):
    lowest = True
    #Up
    if (validate(i,j,'u') and smoke[i-1][j] <= smoke[i][j]): lowest = False
    #Right
    if (validate(i,j,'r') and smoke[i][j+1] <= smoke[i][j]): lowest = False
    #Down
    if (validate(i,j,'d') and smoke[i+1][j] <= smoke[i][j]): lowest = False
    #Left
    if (validate(i,j,'l') and smoke[i][j-1] <= smoke[i][j]): lowest = False
    return lowest

def explore(i,j):
    visited = np.zeros([len(smoke),len(smoke[0])])
    queue = []
    xs = [0, 1, 0, -1]
    ys = [-1, 0, 1, 0]
    dirs = ['u','r','d','l']
    tupo = (i,j)
    queue.append(tupo)
    visited[i][j] = 1
    while (queue):
        s = queue.pop(0)
        global sum
        sum += 1
        for n in range(4):
            if  validate(s[0],s[1],dirs[n]) and visited[s[0]+ys[n]][s[1]+xs[n]] == 0 and smoke[s[0]+ys[n]][s[1]+xs[n]] > smoke[s[0]][s[1]] and int(smoke[s[0]+ys[n]][s[1]+xs[n]]) < 9:
                tupo = (s[0]+ys[n],s[1]+xs[n])
                queue.append(tupo)
                visited[s[0]+ys[n]][s[1]+xs[n]] = 1

for i in range(len(smoke)):
    for j in range(len(smoke[i])):
        if (check_adj(i, j)): 
            if (isPartOne):
                sum+=int(smoke[i][j])+1
            else:
                explore(i,j)
                basins.append(sum)
                sum = 0
    
if (isPartOne): print(sum)
else:
    basins.sort(reverse=True)
    print(basins[0] * basins[1] * basins[2])