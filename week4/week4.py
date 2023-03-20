f = open("devClub/week4/nombres.txt", "r")
grid = [[int(test) for test in lines.split(' ')]
        for lines in f.read().split(' \n')]
final = 0
for i, line in enumerate(grid):
    if (i == 0 or i == len(grid)-1):
        continue
    for j, num in enumerate(line):
        if (j == 0 or j == len(line)-1):
            continue
        ver = grid[i-1][j]*grid[i][j]*grid[i+1][j]
        hor = grid[i][j-1]*grid[i][j]*grid[i][j+1]
        diag1 = grid[i-1][j-1]*grid[i][j]*grid[i+1][j+1]
        diag2 = grid[i+1][j-1]*grid[i][j]*grid[i-1][j+1]
        prov = max(ver, hor, diag1, diag2)
        if (prov > final):
            final = prov
print(final)
