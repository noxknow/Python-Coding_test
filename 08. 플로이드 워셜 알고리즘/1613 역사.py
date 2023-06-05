import sys
sys.stdin=open("input.txt","r")
input = sys.stdin.readline

n, m = map(int, input().split())
prob = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(m):
    start, end = map(int, input().split())
    prob[start][end] = -1
    prob[end][start] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if prob[i][j] == 0:
                if prob[i][k] + prob[k][j] == -2:
                    prob[i][j] = -1
                elif prob[i][k] + prob[k][j] == 2:
                    prob[i][j] = 1

s = int(input())
for i in range(s):
    a, b = map(int, input().split())
    print(prob[a][b])
