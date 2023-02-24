import numpy as np
import heapq as heap
from collections import defaultdict

isPartOne = False
cavern = np.genfromtxt('./inputs/15.txt', delimiter=1, dtype=int)
if not isPartOne:
    new = np.zeros([len(cavern)*5, len(cavern[0])*5])
    for i in range(len(cavern)):
        for j in range(len(cavern[0])):
            for k in range(5):
                for l in range(5):
                    new[i+(k*len(cavern))][j+(l*len(cavern[i]))] = cavern[i][j] + k + l if cavern[i][j]+k+l <= 9 else cavern[i][j] + k + l - 9
    cavern = new

xs = [0, 1, 0, -1]
ys = [1, 0, -1, 0]

def next_node(t, n):
    return tuple(map(lambda a, b: a + b, t, (ys[n], xs[n])))

def validate(t):
    return t[0] >= 0 and t[1] >= 0 and t[0] < len(cavern) and t[1] < len(cavern[0])

def dijkstra():
    visited = set()
    pq = []
    heap.heappush(pq, (0, (0,0)))
    nodeCosts = defaultdict(lambda: float('inf'))
    nodeCosts[(0,0)] = 0
    while pq:
        _, node = heap.heappop(pq)
        visited.add(node)
        for i in range(4):
            next = next_node(node, i)
            if next in visited: continue
            elif validate(next):
                newCost = nodeCosts[node] + cavern[next]
                if nodeCosts[next] > newCost:
                    nodeCosts[next] = newCost
                    heap.heappush(pq, (newCost, next))
    return nodeCosts

print(dijkstra()[len(cavern)-1,len(cavern[0])-1])