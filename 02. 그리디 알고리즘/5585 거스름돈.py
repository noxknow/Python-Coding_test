import sys
input = sys.stdin.readline

money = int(input())
lst = [500, 100, 50, 10, 5, 1]

num = 1000 - money
cnt = 0

for i in range(6): 
    if num != 0:  # 어짜피 나누어 떨어지니 없어도 됨
        cnt += num // lst[i]
        num %= lst[i]
        if num <= 0: # 이하동문
            break # 이하동문

print(cnt)
