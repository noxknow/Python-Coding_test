import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int, input().split())

visited = [0] * (n+1)
cnt = 0
graph = [[] for _ in range(n+1)]
for i in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

def bfs(v):
  visited[v] = 1
  q = deque([(v)])
  
  while q:
    n = q.popleft()
    for nx in graph[n]:
      if visited[nx] == 0:
        visited[nx] = 1
        q.append((nx))
  
for i in range(1,n+1):
  if visited[i] == 0:
    bfs(i)
    cnt += 1

print(cnt)
