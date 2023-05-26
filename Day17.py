import re

bounds = [int(x) for x in re.findall("[-\d]+", open("./inputs/test.txt").read().strip())]
maxtime, min_x_vel = 0, 999999
for x in range(1, bounds[0]):
    time, last, distance = 1, 0, 0
    while (last <= distance):
        last = distance
        distance = -.5 * (time+1) * (time-2*x)
        time += 1
        if min(bounds[0],bounds[1]) <= last <= max(bounds[0], bounds[1] and last % 1 == 0):
            maxtime = max(maxtime, time)
            min_x_vel = min(min_x_vel, x)
    if last > max(bounds[0], bounds[1]):
        break

y, last, distance, max_y_vel = 1, 0, 0, 0
while (y < max(-bounds[2],-bounds[3])):
    last = distance
    distance = -.5 * maxtime * (maxtime-2*y)
    if distance > min(-bounds[2],-bounds[3]) and distance % 1 == 0:
        max_y_vel = max(max_y_vel, y)
    y += 1

print("Maximum Height:", sum(max_y_vel-t for t in range(max_y_vel+1)))

def find_possibles(min_vel, max_vel, x_or_y):
    possibles = []
    for i in range(min_vel, max_vel+1):
        time, x = 0, 0
        if x_or_y==0:
            while (x <= bounds[1] and time<=maxtime):
                x = -.5 * (time+1) * (time-2*i)
                time += 1
                if (bounds[x_or_y] <= x <= bounds[x_or_y+1]):
                    possibles.append(i)
                    break
        else:
            while (x >= bounds[2]):
                x = -.5 * (time+1) * (time-2*i)
                time += 1
                if (bounds[2] <= x <= bounds[3]):
                    possibles.append(i)
                    break
    return possibles

possible_x = find_possibles(min_x_vel, bounds[1], 0)
possible_y = find_possibles(bounds[2], max_y_vel, 1)


def sim(vx, vy, px=0, py=0):
    if px > bounds[1] or py < bounds[2]: return 0
    if px >= bounds[0] and py <= bounds[3]: return 1
    return sim(vx-(vx>0), vy-1, px+vx, py+vy)
hits = [sim(x,y) for x in possible_x for y in possible_y]
print("Total combinations:",sum(hits))