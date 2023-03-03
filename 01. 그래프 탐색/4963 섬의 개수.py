from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]

def bfs(x, y):
    
    q = deque([(x,y)])
    graph[x][y] = 0
    
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
    
while True:
    w, h = map(int, input().split())
    
    if w == 0 and h == 0:
        break
    
    cnt = 0
    graph = []
    for i in range(h):
        graph.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i, j)
                cnt += 1
                
    print(cnt)
                    
