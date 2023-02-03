# BFS
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().strip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    q = deque([(x,y)])
    graph[x][y] = 0
    cnt = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1: # nx,ny로 이동했는데 n을 벗어나면 안된다.
                graph[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1

    return cnt

result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result.append(bfs(i,j))

result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])

# DFS
import sys
input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().strip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0

def dfs(x,y):

    if x < 0 or x >= n or y < 0 or y >= n:
        return 
    
    if graph[x][y] == 1:
        graph[x][y] = 0
        global cnt
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)

result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            dfs(i,j)
            result.append(cnt)
            cnt = 0

result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])