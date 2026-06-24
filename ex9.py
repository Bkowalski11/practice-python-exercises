import random
a = random.randrange(1,99)
b = random.randrange(1,99)
c = []


for x in a:
    if x in b:
        c.append(x)
print(list(set(c)))