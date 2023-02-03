import sys
input = sys.stdin.readline
from collections import deque

def dfs(graph, v):
    visited = {}
    stack = [v]

    while stack: # stack이 비어있을 때 까지 (아래보면 맨 마지막 스택 비어져 있다.)
        n = stack.pop()
        if n not in visited:
            visited.setdefault(n) # 딕셔너리 방식이라 setdefault이고, list였으면 append
            stack += reversed(graph[n]) # 그래프 역수로 넣기
    return visited

def bfs(graph, v):
    visited = {}
    queue = deque([(v)]) 

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.setdefault(n)
            queue += graph[n]
    return visited

n,m,v = map(int, input().split())

graph = [[] for i in range(n+1)] # 그래프 방식을 딕셔너리로도 할 수 있고 list로도 할 수 있는데
for i in range(m): # 그때는 range 범위들이 달라지게 된다. 
    x, y = map(int, input().split()) # n+1개인 이유는 1번 컴퓨터를 1번 인덱스로 쓰기 위해, 1개 더 추가한 것입니다.
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, n + 1): # 맨 아래 써둠
        graph[i].sort()

print(' '.join(list(map(str,dfs(graph, v)))))
print(' '.join(list(map(str,bfs(graph, v)))))

# graph = {i:[] for i in range(1,n+1)} 이게 딕셔너리 방식
# for i in range(1, m+1):
#     x, y = map(int, input().split())
#     graph[x].append(y)
#     graph[y].append(x)

# for key in graph:
#     graph[key].sort()

"""
dfs - stack 방식으로 1 2, 1 3, 1 4, 2 4, 3 4 가 있으면 
visited : 1         1        1 2    1 2    1 2 4     1 2 4 3   
stack   : 2 3 4  -> 4 3 2 -> 4 3 -> 3 4 -> 3      -> 
들어가는 노드(정점)을 역수로 바꿔주면서 방문 처리 한다. 4 3 에서 3 4 가 될때는 2 노드가 들어가면서
4를 부르기 때문에 4가 다시 앞으로 가는거다. 2는 1은 방문처리이니 4하나랑만 간선으로 연결되어 있고,
그래서 역수 취할게 없기 때문에 4 3 이 3 4 로 바뀐다.
bfs 는 그냥 보이는 대로 deque popleft형식으로 

"방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고," 추가되는 간선 
정보가 오름차순이 아니라면 이 조건을 만족하지 못하게 됩니다. (문제에선 당연히 오름차순으로 
주어진다는 보장이 없죠) 따라서 위 조건을 위해 각 정보들을 모두 정렬해주는 것입니다.
"""

# 다른 방식
import sys
input = sys.stdin.readline
from collections import deque

n,m,v = map(int, input().split())

graph = [[] for i in range(n+1)]
for _ in range(m):
    [a,b] = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

visited_dfs = [0] * (n+1) # 0이 false여도 된다.
visited_bfs = [0] * (n+1)

def dfs(v):
    visited_dfs[v] = 1
    print(v, end = " ")

    for i in graph[v]:
        if visited_dfs[i] == 0:
            dfs(i)

def bfs(v):
    q = deque([(v)])
    visited_bfs[v] = 1

    while q:
        v = q.popleft()
        print(v, end = " ")
        for i in graph[v]:
            if visited_bfs[i] == 0:
                q.append(i)
                visited_bfs[i] = 1

dfs(v)
print()
bfs(v)