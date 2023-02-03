import sys
input = sys.stdin.readline

n = int(input())

weigh = []
for i in range(n):
    weigh.append(int(input()))

weigh.sort(reverse = True)

result = []
for i in range(n):
    result.append(weigh[i]*(i+1))

print(max(result))