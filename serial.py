file = open('input-5mil.txt', "r")
n = int(file.readline())
arr_chunk = []


for i in range(n):
    arr_chunk.append(file.readline())

max_len = 0
longest_words = []
for word in arr_chunk:
    if len(word) > max_len:
        max_len = len(word)

for word in arr_chunk:
    if len(word) == max_len:
        longest_words.append(word)