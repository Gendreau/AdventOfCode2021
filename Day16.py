import numpy as np

input = open("./inputs/16.txt").read()
num = (bin(int(input,16))[2:]).zfill(len(input.strip())*4)
versionTotal = 0

def parse(num):
    global versionTotal
    versionTotal, typeID, num = versionTotal + int(num[:3],2), int(num[3:6],2), num[6:]
    if typeID == 4:
        literal = ""
        while num[0] == "1":
            literal, num = literal + num[1:5], num[5:]
        return(num[5:], int(literal + num[1:5],2))
    else:
        lengthTypeID, num = num[0], num[1:]
        subvalues = []
        if lengthTypeID == "0":
            subpackets, num = num[15:15+int(num[:15],2)], num[15+int(num[:15],2):]
            while "1" in subpackets:
                subpackets, subvalue = parse(subpackets)
                subvalues.append(subvalue)
        else:
            subpackets, num = int(num[:11],2), num[11:]
            for i in range(subpackets):
                num, subvalue = parse(num)
                subvalues.append(subvalue)
        if typeID == 0:
            return num, sum(subvalues)
        elif typeID == 1:
            return num, np.prod(subvalues)
        elif typeID == 2:
            return num, min(subvalues)
        elif typeID == 3:
            return num, max(subvalues)
        elif typeID == 5:
            return num, 1 if subvalues[0] > subvalues[1] else 0
        elif typeID == 6:
            return num, 1 if subvalues[0] < subvalues[1] else 0
        elif typeID == 7:
            return num, 1 if subvalues[0] == subvalues[1] else 0

_, value = parse(num)
print("Version Total:", versionTotal)
print("Packet Value:", value)