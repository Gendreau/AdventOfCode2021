import numpy as np
grid = [list(ln) for ln in open('./inputs/25.txt').read().split("\n")]
h, w = len(grid), len(grid[0])

loop, moves = 0, False
no_moves, to_move = np.zeros([h, w], dtype=int), np.zeros([h, w], dtype=int)
to_move[0][0] = 1

while not moves or np.equal(to_move, no_moves).all() == False:
    to_move = np.zeros([h, w], dtype=int)
    moves = False
    for y in range(h):
        for x in range(w):
            if grid[y][x] != '>':
                continue
            if x != w-1 and grid[y][x+1] != '.':
                continue
            if x == w-1 and grid[y][0] != '.':
                continue
            to_move[y][x] = 1
    for y in range(h):
        for x in range(w):
            if to_move[y][x] != 1:
                continue
            grid[y][x] = '.'
            if x == w-1:
                grid[y][0] = '>'
            else:
                grid[y][x+1] = '>'
    moves = np.equal(to_move, no_moves).all()
    to_move = np.zeros([h, w], dtype=int)
    for y in range(h):
        for x in range(w):
            if grid[y][x] != 'v':
                continue
            if y != h-1 and grid[y+1][x] != '.':
                continue
            if y == h-1 and grid[0][x] != '.':
                continue
            to_move[y][x] = 1
    for y in range(h):
        for x in range(w):
            if to_move[y][x] != 1:
                continue
            grid[y][x] = '.'
            if y == h-1:
                grid[0][x] = 'v'
            else:
                grid[y+1][x] = 'v'
    loop += 1

print(loop)