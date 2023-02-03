from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().strip())))

visited = [[False for _ in range(m)] for _ in range(n)] # n * m
# visited = [[False for _ in range(n)] for _ in range(m)] 이거는 m * n 이다.

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque([(x,y,1)])
    visited[x][y] = True

    while queue:
        x, y, distance = queue.popleft() # queue.append에서 계속 queue값이 들어오고 거기서 가장 왼쪽 값들 다 빼오기
        if x == n-1 and y == m-1:
            print(distance)
            break
        else:
            for i in range(4): 
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx,ny,distance+1))                  
bfs(0,0)


# 다른 방식
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())

maze = []
for _ in range(n):
    maze.append(list(map(int, input().strip())))

def bfs(x, y):
    # 상, 하, 좌, 우 (0,0) -> (1,0) 생각해보면 행이 하나 늘면서 아래로 갈 때 x좌표는 +1 즉, 아래가 +1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque([(x, y)])
    
    while queue:
        x, y = queue.popleft() 
        #갈 수 있는 방향 찾기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #갈 수 있는 곳이라면
            if 0 <= nx < n and  0 <= ny < m and maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
    return maze[n-1][m-1]

print(bfs(0, 0))