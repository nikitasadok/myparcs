import random

file = open('input-1mil.txt', "r")
num_words = int(file.readline())
arr_chunk = []

for i in range(num_words):
    arr_chunk.append(file.readline())

z_funcs = []
for word in arr_chunk:
    n = len(word)
    z = []
    for i in range(n):
        z.append(0)

    for i in range (1, n):
        while (i + z[i] < n and word[z[i]] == word[i + z[i]]):
            z[i] += 1
        z_funcs.append("".join(str(x) for x in z[:(n-1)]))
