import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    case = []
    n = int(input())
    for _ in range(n):
        [a,b] = map(int, input().split())
        case.append([a,b])

    case.sort(key=lambda x: x[0])

    last = case[0][1]
    cnt = 0
    for i,j in case:
        if j <= last:
            cnt += 1
            last = j
    print(cnt)

# 다른 방법
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    rank = []
    for i in range(n):
        a, b = map(int, input().split())
        rank.append([a,b])
    
    rank.sort(key=lambda x: x[0])
    result = 1
    score = rank[0][1]
    for i in range(1,n):
        if score > rank[i][1]:
            score = rank[i][1]
            result += 1
    
    print(result)
