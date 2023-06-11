import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def bfs(x, y, visited, grpah):
    global moved
    people = graph[x][y]
    cnt = 1
    q = deque([(x,y)])
    visited[x][y] = True
    temp = list()
    temp.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if visited[nx][ny]:
                continue

            if l <= abs(grpah[x][y] - grpah[nx][ny]) <= r:
                visited[nx][ny] = True
                q.append((nx, ny))
                people += graph[nx][ny]
                cnt += 1
                temp.append((nx, ny))

    move_people = people // cnt

    if cnt > 1: # people = graph[x][y] 이 부분에 의해서 하나는 무조건 들어간다. 그 경우 빼주기 위해 > 1
        moved = True
        for x, y in temp:
            graph[x][y] = move_people

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

moved = False
answer = 0

while True:
    moved = False
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j, visited, graph)

    if moved:
        answer += 1
    else:
        break

print(answer)
