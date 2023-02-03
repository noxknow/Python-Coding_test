# BFS
import sys
input = sys.stdin.readline
from collections import deque

t = int(input())

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
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx,ny))
                cnt += 1
    return cnt

for _ in range(t):
    n,m,k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)] # n*m 이다.

    for i in range(k):
        a,b = map(int, input().split())
        graph[a][b] = 1
    
    result = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                result.append(bfs(i,j))

    print(len(result))

# DFS
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000) # 런타임 오류가 발생하는걸 방지(recursion error 재귀 깊이가 깊을때 에러가 발생)

t = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x,y):

    if x < 0 or x >= n or y < 0 or y >= m:
        return

    if graph[x][y] == 1:
        graph[x][y] = 0
        global cnt
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)

for _ in range(t):
    n,m,k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    cnt = 0

    for _ in range(k):
        a,b = map(int, input().split())
        graph[a][b] = 1

    result = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                dfs(i,j)
                result.append(cnt)
                cnt = 0
    
    print(len(result))