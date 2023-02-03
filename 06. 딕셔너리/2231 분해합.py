n = int(input())
res = 0

for i in range(1, n+1):
    A = list(map(int, str(i)))
    tmp = i + sum(A)
    if tmp == n:
        res = i
        break

print(res)