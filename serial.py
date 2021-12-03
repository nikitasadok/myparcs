import random

file = open('input-5mil2.txt', "r")
num_words = int(file.readline())
arr_chunk = []

strs = []
n = 50
for i in range(num_words):
    s = ''
    for j in range(random.randint(6, n)):
        letter = random.randint(65, 123)
        s += str(chr(letter))
    strs.append(s)

max_len = 0
longest_words = []
for word in strs:
    if len(word) > max_len:
        max_len = len(word)

for word in strs:
    if len(word) == max_len:
        longest_words.append(word)