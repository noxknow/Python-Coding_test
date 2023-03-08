from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque([(x,y)])
    visited[x][y] = 1
    cnt = 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny] >= k and visited[nx][ny] == 0:
                q.append((nx,ny))
                visited[nx][ny] = 1
                cnt += 1

    return cnt

n = int(input())
max_num = 0
answer = 0

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] > max_num:
            max_num = graph[i][j]

for k in range(1, max_num+1):
    res = []
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= k and visited[i][j] == 0:
                res.append(bfs(i,j))
    answer = max(answer, len(res))

print(answer)
