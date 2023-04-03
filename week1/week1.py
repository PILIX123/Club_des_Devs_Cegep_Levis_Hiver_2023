with open("week1/instructions.txt", "r") as instruction:
    string = instruction.read()
    total = 0
    for char in string:
        if(char == "("):
            total+=1
        else:
            total-=1
    print(total)