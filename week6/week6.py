fruits = dict()
x = 420
with open('week6/fruits.txt', "r", encoding='utf-8') as f:
    li = f.read().splitlines()
    for line in li:
        (key, val) = line.split('-', 1)
        fruits.update({int(key): val})

while x not in fruits:
    digsum = sum([int(dig) for dig in str(x)])
    x -= digsum

print(fruits.get(x))
