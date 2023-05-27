import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
cum = [nums[0]]
for i in range(1, n):
    cum.append(cum[-1]+nums[i])

m = int(input())
for _ in range(m):
    i, j = map(int, input().split())
    if i == 1:
        print(cum[j-1])
    else:
        print(cum[j-1]-cum[i-2])
