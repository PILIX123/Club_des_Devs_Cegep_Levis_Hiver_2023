total = 0
dim = list()
with open("devClub/week7/phrases.txt", "r") as phrases:
    dim = phrases.read().splitlines()
for phrase in dim:
    if(len(list(dict.fromkeys(list(phrase.replace(" ",""))))) == 26):
        total+=1

print(total)
