import sys
input = sys.stdin.readline

n, k = map(int, input().split())
num = []
for i in range(n):
    num.append(int(input()))

dp = [0] * (k+1)
dp[0] = 1

for c in num:
    for i in range(1, k+1):
        if i-c >= 0:
            dp[i] += dp[i-c]
print(dp[k])
