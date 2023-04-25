import sys
input = sys.stdin.readline

n,m = map(int, input().split())
num = list(map(int, input().split()))
sum_num = []
sum = 0
for i in range(n):
    sum += num[i]
    sum_num.append(sum)
    
for i in range(m):
    res = 0
    x, y = map(int, input().split())
    if x<2 :
        res = sum_num[y-1]
    else :
        res = sum_num[y-1] - sum_num[x-2]
    print(res)
