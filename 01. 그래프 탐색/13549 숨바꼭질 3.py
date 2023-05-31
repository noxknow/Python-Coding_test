import sys
from collections import deque
sys.stdin=open("input.txt","r")
input = sys.stdin.readline

n, k = map(int, input().split())
q = deque()
q.append(n)
MAX = 100001
visited = [0] * MAX
distance = [0] * MAX
visited[n] = 1

while q:
    tmp = q.popleft()
    if tmp*2<=MAX-1 and visited[tmp*2] == 0:
        q.appendleft(tmp*2)
        visited[tmp*2] = 1
        distance[tmp*2] = distance[tmp]
    if tmp+1<=MAX-1 and visited[tmp+1] == 0:
        q.append(tmp+1)
        visited[tmp+1] = 1
        distance[tmp+1] = distance[tmp] + 1
    if tmp-1>=0 and visited[tmp-1] == 0:
        q.append(tmp-1)
        visited[tmp-1] = 1
        distance[tmp-1] = distance[tmp] + 1

print(distance[k])
