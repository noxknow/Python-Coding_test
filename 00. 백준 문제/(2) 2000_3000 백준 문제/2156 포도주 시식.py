import sys 
input = sys.stdin.readline

n = int(input())
num = [0] * (n+2)
for i in range(n):
    num[i] = int(input())

dp = [0] * (n+2)
dp[0] = num[0]
dp[1] = num[0] + num[1]
dp[2] = max(num[0]+num[2], num[2]+num[1], dp[1])

for i in range(3, n):
    dp[i] = max(dp[i-2]+num[i], dp[i-3]+num[i-1]+num[i], dp[i-1])

print(max(dp))
