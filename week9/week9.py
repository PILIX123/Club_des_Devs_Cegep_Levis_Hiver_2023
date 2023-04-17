inputpath = "week9/jeu.txt"
with open(inputpath, "r") as games:
    global fixed
    fixed = [i.split() for i in games.read().split("\n")]


score1 = 0
score2 = 0
"""
A = rock
B = Paper
C = Scissors
X = Rock
Y = Paper
Z = Scissors
0 = lost
3 = draw
6 = won
"""
scoring2 = {
    'X': 1,
    'Y': 2,
    'Z': 3
}
scoring1 = {
    'A': 1,
    'B': 2,
    'C': 3
}
win = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
}
draw = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}
loose = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
}
for game in fixed:
    score1, score2 = (10+score1, 0+score2) if win.get(game[0]) == game[1] else (
        5 + score1, 5+score2) if draw.get(game[0]) == game[1] else (0+score1, 10+score2)
    score1 += scoring1.get(game[0])
    score2 += scoring2.get(game[1])

print(score1 if score1 > score2 else score2)
