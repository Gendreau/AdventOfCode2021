import numpy as np
import sys

transparent = np.genfromtxt('./inputs/13.txt', delimiter=',', dtype=int, invalid_raise=False)
isPartOne = False
if isPartOne: folds = [['x',655]]
else: folds = [['x',655], ['y',447], ['x',327], ['y',223], ['x',163], ['y',111], ['x',81], ['y',55], ['x',40], ['y',27], ['y',13], ['y',6]]


for dot in transparent:
    for fold in folds:
        if fold[0] == 'y':
            dot[1] = 2*fold[1]-dot[1] if dot[1] > fold[1] else dot[1]
        elif fold[0] == 'x':
            dot[0] = 2*fold[1]-dot[0] if dot[0] > fold[1] else dot[0]

if isPartOne:
    print(len(np.unique(transparent, axis=0)))
else:
    np.set_printoptions(threshold=sys.maxsize, linewidth=40)
    np.swapaxes(transparent, 0, 1)
    transparent = np.unique(transparent, axis=0)
    transparent = [tuple(x) for x in transparent]
    lastx=0
    lasty=0
    display = []
    for i in range(6):
        subdisplay = ""
        for j in range(39):
            if (j,i) in transparent: subdisplay += "#"
            else: subdisplay += " "
        display.append(subdisplay)
    for x in display:
        print(x)