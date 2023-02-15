import sys
input = sys.stdin.readline

n = int(input())

coor = []
for _ in range(n):
    num = list(map(int, input().split()))
    coor.append(num)

coor.sort()

for i in range(n):
    print(coor[i][0], coor[i][1])

