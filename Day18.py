import math

with open('./inputs/18.txt') as f: lines = list(filter(None, f.read().split('\n')))
lines_list = []
for line in lines:
    sublist = []
    for char in line:
        sublist.append(char)
    lines_list.append(sublist)

class Snailfish:
    def __init__(self, num):
        self.num = num
    
    def add(self, new_num):
        self.num = ["["] + self.num + [","] + new_num + ["]"]

    def try_explode_split(self):
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
                return False
            elif ch == '[':
                level += 1
            elif ch == ']':
                level -= 1
        for idx, ch in enumerate(self.num):
            if ch.isnumeric() and int(ch) >= 10:
                leftSplit, rightSplit = str(math.floor(int(ch)/2)), str(math.ceil(int(ch)/2))
                self.num = self.num[:idx] + ["["] + [leftSplit] + [","] + [rightSplit] + ["]"] + self.num[idx+1:]
                return False
        return True
    
    def find_magnitude(self):
        for idx, ch in enumerate(self.num):
            if idx+2 < len(self.num) and ch.isnumeric() and self.num[idx+2].isnumeric():
                self.num = self.num[:idx-1] + [str(int(ch)*3 + int(self.num[idx+2])*2)] + self.num[idx+4:]
                return False
        return True


sfn = Snailfish(lines_list[0])
for i in lines_list[1:]:
    sfn.add(i)
    while(sfn.try_explode_split() == False):
        continue
while(sfn.find_magnitude() == False):
    continue
print(sfn.num[0])

max_magnitude = 0
for n1 in lines_list:
    for n2 in lines_list:
        if n1 == n2: continue
        sfn1 = Snailfish(n1)
        sfn1.add(n2)
        while(sfn1.try_explode_split() == False):
            continue
        while(sfn1.find_magnitude() == False):
            continue
        max_magnitude = max(max_magnitude, int(sfn1.num[0]))
print(max_magnitude)