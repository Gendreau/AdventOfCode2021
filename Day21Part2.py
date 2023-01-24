import math

#mostly stolen from u/jonathan_paulson

player1 = 2 - 1
player2 = 5 - 1
spaces = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
memo = {}

def win(player1, player2, score1, score2):
    if (score1 >= 21):
        return (1,0)
    if (score2 >= 21):
        return (0,1)
    if (player1, player2, score1, score2) in memo:
        return memo[(player1, player2, score1, score2)]
    answer = (0,0)
    for d1 in range(1,4):
        for d2 in range(1,4):
            for d3 in range(1,4):
                p1new = (player1 + d1 + d2 + d3) % 10
                s1new = score1 + p1new + 1

                x, y = win(player2, p1new, score2, s1new)
                answer = (answer[0] + y, answer[1] + x)
    memo[(player1, player2, score1, score2)] = answer
    return answer

print(max(win(player1, player2, 0, 0)))