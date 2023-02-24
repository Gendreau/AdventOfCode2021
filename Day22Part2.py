import re

commands = []
for line in open("./inputs/22.txt").readlines():
    a = 1 if line.split()[0] == "on" else 0
    b, c, d, e, f, g = map(int, re.findall("-?\d+", line))
    commands.append(list((a, b, c, d, e, f, g)))

cubes = []

class Cube:
    def __init__(self, toggle, xlow, xhigh, ylow, yhigh, zlow, zhigh):
        self.toggle = toggle
        self.xlow = xlow
        self.xhigh = xhigh
        self.ylow = ylow
        self.yhigh = yhigh
        self.zlow = zlow
        self.zhigh = zhigh
    
    def overlap(self, cubes):
        volume = abs((self.xhigh-self.xlow+1)*(self.yhigh-self.ylow+1)*(self.zhigh-self.zlow+1))
        for cube in cubes:



for command in reversed(commands):
    cube = Cube(commands[0], commands[1],commands[2],commands[3],commands[4],commands[5],commands[6],commands[7])
    cube.



print(sum(cubes.values()))