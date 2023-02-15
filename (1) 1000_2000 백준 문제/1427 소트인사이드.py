n = list(map(int, input()))

num = []
for i in n:
    num.append(i)

num.sort(reverse =True)

for i in num:
    print(i, end = "")

