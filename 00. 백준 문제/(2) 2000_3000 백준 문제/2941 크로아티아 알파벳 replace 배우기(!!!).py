words = input()
alpabet_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for x in alpabet_list:
    words = words.replace(x, "a")

print(len(words))