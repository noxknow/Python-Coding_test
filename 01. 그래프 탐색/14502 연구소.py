import sys
import copy
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def makeWall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                board[i][j] = 1
                makeWall(cnt + 1)
                board[i][j] = 0

def bfs():
    q = deque()
    test_board = copy.deepcopy(board)
    for i in range(n):
        for j in range(m):
            if test_board[i][j] == 2:
                q.append((i,j))

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and test_board[nx][ny] == 0:
                q.append((nx,ny))
                test_board[nx][ny] = 2
                
    global res
    cnt = 0
    for i in range(n):
        for j in range(m):
            if test_board[i][j] == 0:
                cnt += 1
    res = max(res, cnt)

res = 0
makeWall(0)
print(res)
