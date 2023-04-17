total = 0
fib = 1
prev = 0
while fib < 1000000:
    if fib % 2 > 0:
        total += fib
    tmp = fib
    fib += prev
    prev = tmp
print(total)
