import sys
input = sys.stdin.readline
# sys.setrecursionlimit(100000)

n = int(input())

sol = [0] * 1001
sol[1] = 1
sol[2] = 2

for i in range(3, 1001):
    sol[i] = sum(sol[i-2 : i])

print(sol[n] % 10007)

# def sol(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     else:
#         return sol(n-1) + sol(n-2)

# print(sol(n)%10007)