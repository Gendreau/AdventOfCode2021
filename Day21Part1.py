import math

space1 = 2
space2 = 5
player1 = player2 = 0
dice = 0
spaces = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def checkWin(player1, player2):
    global turn
    if player1 >= 1000:
        print(player2 * dice)
        raise SystemExit(0)
    elif player2 >= 1000:
        print(player1 * dice)
        raise SystemExit(0)
    else: return

def roll():
    global dice
    dice += 1
    return dice

while (True):
    space1 += roll() + roll() + roll()
    space1 %= 10
    player1 += spaces[space1]
    checkWin(player1, player2)
    space2 += roll() + roll() + roll()
    space2 %= 10
    player2 += spaces[space2]
    checkWin(player1, player2)