import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
for _ in range(m):
    board.append(list(input().strip()))
    
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,a):
    q = deque([(x,y,a)])
    board[x][y] = 0
    cnt = 1
    
    while q:
        x, y, a = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n and board[nx][ny] == a:
                q.append((nx,ny,a))
                board[nx][ny] = 0
                cnt += 1
    return cnt*cnt

sumW = 0
sumB = 0
for i in range(m):
    for j in range(n):
        if board[i][j] == "W":
            sumW += bfs(i,j,"W")
        elif board[i][j] == "B":
            sumB += bfs(i,j,"B")

print(sumW, sumB) 
