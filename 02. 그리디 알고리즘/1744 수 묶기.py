n = int(input())
plus = []
minus = []
res = 0
for i in range(n):
    x = int(input())
    if x <= 0:
        minus.append(x)
    elif x == 1:
        res += x
    else:
        plus.append(x)

plus.sort(reverse=True)
minus.sort()
if len(plus)%2 != 0:
    plus.append(1)
if len(minus)%2 != 0:
    minus.append(1)
for i in range(0, len(plus), 2):
    res += plus[i]*plus[i+1]
for i in range(0, len(minus), 2):
    res += minus[i]*minus[i+1]

print(res)
