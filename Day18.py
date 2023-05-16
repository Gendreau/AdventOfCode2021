import math

lines = [list(x) for x in open('./inputs/18.txt').read().splitlines()]

class Snailfish:
    def __init__(self, num):
        self.num = num
    
    def add(self, new_num):
        self.num = ["["] + self.num + [","] + new_num + ["]"]

    def explode_split(self):
        level = 0
        for idx, ch in enumerate(self.num):
            if level == 5:
                left, right, i = int(ch), int(self.num[idx+2]), 3
                while idx+i < len(self.num) and not self.num[idx+i].isnumeric():
                    i += 1
                if idx+i < len(self.num):
                    self.num = self.num[:idx+i] + [str(int(self.num[idx+i]) + right)] + self.num[idx+i+1:]
                i = 1
                while not self.num[idx-i].isnumeric() and idx-i > 0:
                    i += 1
                if idx-i > 0:
                    self.num = self.num[:idx-i] + [str(int(self.num[idx-i])+left)] + self.num[idx-i+1:]
                self.num = self.num[:idx-1] + ["0"] + self.num[idx+4:]
                return self.explode_split()
            elif ch == '[':
                level += 1
            elif ch == ']':
                level -= 1
        for idx, ch in enumerate(self.num):
            if ch.isnumeric() and int(ch) >= 10:
                leftSplit, rightSplit = str(math.floor(int(ch)/2)), str(math.ceil(int(ch)/2))
                self.num = self.num[:idx] + ["["] + [leftSplit] + [","] + [rightSplit] + ["]"] + self.num[idx+1:]
                return self.explode_split()
        return
    
    def find_magnitude(self):
        for idx, ch in enumerate(self.num):
            if idx+2 < len(self.num) and ch.isnumeric() and self.num[idx+2].isnumeric():
                self.num = self.num[:idx-1] + [str(int(ch)*3 + int(self.num[idx+2])*2)] + self.num[idx+4:]
                return self.find_magnitude()
        return int(self.num[0])


sfn = Snailfish(lines[0])
for i in lines[1:]:
    sfn.add(i)
    sfn.explode_split()
print(sfn.find_magnitude())

max_magnitude = 0
for n1 in lines:
    for n2 in lines:
        if n1 == n2: continue
        sfn1 = Snailfish(n1)
        sfn1.add(n2)
        sfn1.explode_split()
        max_magnitude = max(max_magnitude, sfn1.find_magnitude())
print(max_magnitude)