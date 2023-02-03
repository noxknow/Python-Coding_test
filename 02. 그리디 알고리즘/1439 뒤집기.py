import sys
input = sys.stdin.readline

s = list(input().strip())

cnt = 0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        cnt += 1

print((cnt+1) //2)

# 다른 방법 
import sys
input = sys.stdin.readline

s = input().strip()
result0 = 0
result1 = 0

if s[0] == "0":
    result1 += 1  #1로 바꾸는 경우
else:
    result0 += 1 # 첫번째가 1인데, 0으로 바꾸는 경우

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == "1":
            result0 += 1 #0으로 바꾸는 경우
        else:
            result1 += 1 #1로 바꾸는 경우

print(min(result0,result1))

