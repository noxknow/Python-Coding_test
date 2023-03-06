from collections import deque
import sys
input = sys.stdin.readline

n,m,k,x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    
visited = [0] * (n+1)

def bfs(x):
    res = []
    q = deque([(x, 0)])
    visited[x] = 1
    
    while q:
        n, distance = q.popleft()
        if distance == k:
            res.append(n)
        for nx in graph[n]:
            if visited[nx] == 0 :
                q.append((nx, distance+1))
                visited[nx] = 1
    
    if len(res) == 0:
        print(-1)
    else:
        res.sort()
        for i in range(len(res)):
            print(res[i], end = "\n")     

bfs(x)
