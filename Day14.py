import numpy as np
import math

s, *p = open('./inputs/14.txt')
str = s.strip()
dtype = np.rec.fromrecords([['AA', 'A']]).dtype
conv = np.loadtxt(p, skiprows=1, usecols=(0, 2), dtype=dtype)
convMap = {}
pairMap = {}
newPairMap = {}
totalMap = {}
steps = 40

for key, value in conv:
    convMap[key] = value
    pairMap[key] = 0
    totalMap[value] = 0
newPairMap = pairMap.copy()

for i in range(2, len(str)+1):
    pairMap[str[i-2:i]] += 1

for i in range(steps):
    for key in pairMap.keys():
        newKeyA = key[0] + convMap[key]
        newKeyB = convMap[key] + key[1]
        newPairMap[newKeyA] += pairMap[key]
        newPairMap[newKeyB] += pairMap[key]
    pairMap = newPairMap.copy()
    newPairMap = dict.fromkeys(newPairMap, 0)

for key in pairMap.keys():
    totalMap[key[0]] += pairMap[key]/2
    totalMap[key[1]] += pairMap[key]/2

for key in totalMap.keys():
    totalMap[key] = math.ceil(totalMap[key])

print(max(totalMap.values()) - min(totalMap.values()))