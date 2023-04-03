with open("week8/100x50digits.txt", "r") as digits:
    numbers = [int(res) for res in digits.read().splitlines()]


summed = sum(numbers)
val1 = int(str(sum(numbers))[:5])
val2 = int(str(sum(numbers))[-5:])
print(val1+val2)
