import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
dp = [0] * (n)
dp1 = [1] * (n)
dp2 = [1] * (n)

for i in range(1, n):
    for j in range(i):
        if num[i] > num[j]:
            dp1[i] = max(dp1[i], dp1[j]+1)
            
num.reverse()
for i in range(1, n):
    for j in range(i):
        if num[i] > num[j]:
            dp2[i] = max(dp2[i], dp2[j]+1)
dp2.reverse()

for i in range(n):      
    dp[i] = dp1[i] + dp2[i] 
    
print(max(dp) - 1)
