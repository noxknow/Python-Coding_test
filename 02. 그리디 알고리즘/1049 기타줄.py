import sys
input = sys.stdin.readline

n,m = map(int, input().split())

cost = []
for _ in range(m):
    [a, b] = map(int, input().split())
    cost.append([a,b])

six_list = sorted(cost, key=lambda x: x[0])
one_list = sorted(cost, key=lambda x: x[1])

result = 0
if six_list[0][0] <= one_list[0][1] * 6:
    result = six_list[0][0] * (n // 6) + (n % 6) * one_list[0][1]
    if (n % 6) * one_list[0][1] > six_list[0][0]:
        result = six_list[0][0] * ((n // 6)+1)
else:
    result = one_list[0][1] * n

print(result)

# 다른 방법
import sys
input = sys.stdin.readline

n,m = map(int, input().split())

six_list = []
one_list = []
for _ in range(m):
    [a, b] = map(int, input().split())
    six_list.append(int(a))
    one_list.append(int(b))

six = min(six_list)
one = min(one_list)

# 이하 동문
