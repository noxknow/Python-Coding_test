# 방법 1
t = int(input())

def sol(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return sol(n-1) + sol(n-2) + sol(n-3)

for _ in range(t):
    n = int(input())
    print(sol(n))

# 방법 2
import sys
read = sys.stdin.readline

cache = [0] * 11
cache[1] = 1
cache[2] = 2
cache[3] = 4

for i in range(4, 11):
    cache[i] = sum(cache[i-3:i])

T = int(read())
for _ in range(T):
    print(cache[int(read())])

"""
1 = (1) -> 1개
2 = (1 + 1), (2) -> 2개
3 = (1 + 1 + 1), (1 + 2), (2 + 1), (3) -> 4개
4 = (1 + 1 + 1 + 1), (1 + 1 + 2), (1 + 2 + 1), (1 + 3), (2 + 1 + 1), (2 + 2), (3 + 1) -> 7개

4번째 숫자는 첫번째 + 두번째 + 세번째 로 표현된다.

n이 3보다 클 때 f(n) = f(n-1) + f(n-2) + f(n-3)
"""