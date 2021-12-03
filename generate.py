import random

n = 15
N = 1000000

strs = []
for i in range(N):
    print(i)
    s = ''
    for j in range(random.randint(6, n)):
        letter = random.randint(65, 123)
        s += str(chr(letter))
    strs.append(s)


f = open("input-1mil.txt", "a")
f.write("\n".join(strs))

    
