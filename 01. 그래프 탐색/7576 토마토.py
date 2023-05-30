import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
q = deque()
res = 0

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i,j))

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))

bfs()
res = max(map(max, graph)) - 1
for tmp in graph:
    for t in tmp:
        if t == 0:
            res = -1
print(res)
    
