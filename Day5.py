import numpy as np

ls = np.fromregex(open('./inputs/5.txt'), '\d+', [('',int)]*4)
grid = np.zeros([1000, 1000], dtype=int)
for x1, y1, x2, y2 in ls:
    xstep = 1 if x2>=x1 else -1
    ystep = 1 if y2>=y1 else -1
    if (x1==x2):
        for y in range(y1, y2+ystep, ystep):
            grid[x1][y] += 1
    elif (y1==y2):
        for x in range(x1, x2+xstep, xstep):
            grid[x][y1] += 1
    else:
        for x, y in zip(range(x1,x2+xstep, xstep), range(y1,y2+ystep, ystep)):
            grid[x][y] += 1
print((grid>=2).sum())