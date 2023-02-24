import re

commands = []
for line in open("./inputs/22.txt").readlines():
    a = 1 if line.split()[0] == "on" else 0
    b, c, d, e, f, g = map(int, re.findall("-?\d+", line))
    commands.append(list((a, b, c, d, e, f, g)))

cubes = {}
for command in commands:
    if not (command[2] < -50 or command[1] > 50
      or command[4] < -50 or command[3] > 50
      or command[6] <-50 or command[5] > 50):
        for x in range(command[1],command[2]+1):
            for y in range(command[3],command[4]+1):
                for z in range(command[5],command[6]+1):
                    x, y, z = max(x,-50), max(y,-50), max(z,-50)
                    x, y, z = min(x,50), min(y,50), min(z,50)
                    cubes[(x,y,z)] = command[0]
print(sum(cubes.values()))