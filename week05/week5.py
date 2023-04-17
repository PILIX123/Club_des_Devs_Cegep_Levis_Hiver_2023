import hashlib
num = 0
total = 0
while num < 2000000:
    if ("EFFACE" in hashlib.sha512(str(num).encode()).hexdigest().upper()):
        total += num
    num += 1
print(total)
