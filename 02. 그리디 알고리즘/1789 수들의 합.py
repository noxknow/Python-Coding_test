# 방법 1
import sys
input = sys.stdin.readline

s = int(input())
result = 0
cnt = 0

while True:
    cnt += 1
    result += cnt
    if result >= s:
        break

print(cnt-1)

# 방법 2
import sys
input = sys.stdin.readline

s = int(input())

num = 0
cnt = 0
for i in range(1, s):
    num += i
    cnt += 1
    if s <= num:
        break

print(cnt-1)

