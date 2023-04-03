import math
total = 0
with open("week3/dimensions.txt", "r") as instruction:
    dim = instruction.read().splitlines()
    for dims in dim:
        lSize = list(map(int, dims.split('x')))
        L, l, h = lSize
        lSize.sort()
        sub = 2*L*l + 2*l*h + 2*h*L
        extra = math.ceil((lSize[0]*lSize[1])/3)
        tot = sub+extra
        total += tot
print(total)
