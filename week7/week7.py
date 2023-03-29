import string
from unicodedata import normalize
total = 0
dim = list()
with open("week7/phrases.txt", "r") as phrases:
    dim = phrases.read().splitlines()
for phrase in dim:
    if(len(list(dict.fromkeys(list(normalize("NFD",phrase.translate(str.maketrans('', '', string.punctuation)).replace(" ",'')).lower())))) == 26):
        total+=1

print(total)
