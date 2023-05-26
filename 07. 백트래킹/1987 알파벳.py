import sys
sys.stdin=open("input.txt","r")
input = sys.stdin.readline

def dfs(x,y,cnt):
    global Max
    if Max < cnt:
        Max = cnt
        
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and visited[graph[nx][ny]] == 0:
            visited[graph[nx][ny]] = 1
            dfs(nx,ny,cnt+1)
            visited[graph[nx][ny]] = 0

r,c = map(int,input().split())
graph = [list(map(lambda a : ord(a)-65,input().strip())) for _ in range(r)]
visited = [0]*26

dx = [0,0,1,-1]
dy = [1,-1,0,0]

Max = 1
visited[graph[0][0]] = 1
dfs(0,0,Max)

print(Max)

