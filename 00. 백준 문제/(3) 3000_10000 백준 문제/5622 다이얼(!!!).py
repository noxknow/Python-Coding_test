words = input().upper()
n_words = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

time = 0
for x in n_words:
    for y in x:
        for z in words:
            if y == z:
                time += n_words.index(x)+3

print(time)