# DFS로 푸는 경우
import sys
input = sys.stdin.readline

n = int(input()) # 컴퓨터 개수
v = int(input()) # 연결선 개수

graph = [[] for i in range(n+1)] # 경로를 저장하기 위한 2차원(이중) 리스트, 그래프 초기화
visited = [0]*(n+1) # 방문한 컴퓨터인지 표시
for i in range(v): # 그래프 생성
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    visited[v]=1
    for nx in graph[v]:
        if visited[nx]==0:
            dfs(nx)
            
dfs(1)
print(sum(visited)-1)

# DFS 내 버젼
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    visited = {}
    stack = [v]
    cnt = -1

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.setdefault(n)
            stack += reversed(graph[n])
            cnt += 1
    return cnt

print(dfs(1))

"""
graph 빈 리스트가 n+1개인 이유는 1번 컴퓨터를 1번 인덱스로 쓰기 위해, 1개 더 추가한 것입니다.
위 예제에 대한 그래프는 아래와 같은 이중 리스트로 표현됩니다. 0번 컴퓨터는 없으니, 맨 앞에는 
빈 리스트입니다. 1번 컴퓨터는 2번과 5번에 연결되어 있으니 [2, 5]를 값으로 가집니다. 
이렇게 인덱스가 컴퓨터 번호이고, 값이 연결된 컴퓨터의 리스트인 이중 리스트입니다.
[[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]

여기서 dfs함수에 visited를 인자로 입력받지도 않고, return하지도 않았는데 어떻게 
print(sum(visited)-1)이 정답이 될 수 있는지 궁금할 수 있습니다. visited는 리스트로 파이썬의 
리스트는 함수 밖에서 선언되어, 함수 내부에서 변경되어도, 함수 밖에서 변경이 적용됩니다. 
즉, dfs함수 내부에서 변경된 visited 리스트는 함수 밖에서도 변경이 적용되기 때문에, 
sum(visited) - 1이 정답이 될 수 있습니다. -1 한 이유는 1번 컴퓨터를 제외하고, 
1번 컴퓨터와 연결된 컴퓨터 개수를 출력해야 하기 때문입니다.
"""

# BFS로 푸는 경우
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n+1)

def bfs(v):
    visited[v] = 1
    q = deque([(v)])
    
    while q:
        n = q.popleft()
        for nx in graph[n]:
            if visited[nx] == 0:
                visited[nx] = 1
                q.append(nx)
    return visited

bfs(1)
print(sum(visited) - 1)

# BFS 내 버젼
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(v):
    visited = {}
    q = deque([(v)])
    cnt = -1
    
    while q:
        n = q.popleft()
        if n not in visited:
            q += graph[n]
            visited.setdefault(n)
            cnt += 1
    return cnt


print(bfs(1))

