import random

n = list(range(3, 20))
x = random.choice(n)
y = str()
for i in range(x):
    for j in range(x):
        if x % ((i+1) + (j+1)) == 0 and j > i:
            y = y + str(i+1) + str(j+1)

print(x, y)