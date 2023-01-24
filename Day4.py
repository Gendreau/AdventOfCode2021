import numpy as np

n, *b = open("./inputs/4.txt")
nums = np.loadtxt([n], delimiter=',')
boards = np.loadtxt(b).reshape(-1,5,5)
isPartOne = True
bingos = []

def calc_bingo(board, num):
    score = sum(x for x in np.nditer(board) if x>0) * num
    print(score)
    raise SystemExit(0)

for i in nums:
    for e in np.ndindex(boards.shape):
        if (e[0] in bingos):
            continue
        elif (boards[e] == i):
            boards[e] = -1
            if (sum(boards[e[0]][e[1]][x] for x in range(5)) == -5.0 or sum(boards[e[0]][y][e[2]] for y in range(5)) == -5.0):
                if isPartOne or len(boards)-len(bingos)==1:
                    calc_bingo(boards[e[0]],i)
                else:
                    if e[0] not in bingos:
                        bingos.append(e[0])