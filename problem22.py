#Name Scorer
from string import ascii_letters
alpha=list(ascii_letters[0:26])

with open("0022_names.txt") as f:
    contents=f.read().strip().split(",")

contents.sort()
print(contents[3])
for x in contents:
    for i in x:
        if i in alpha:
            position=alpha.index(i)
            print(position)