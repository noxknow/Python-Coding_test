from collections import deque

def solution(n, wires):
    
    graph = [[] for _ in range(n+1)]
    for x, y in wires:
        graph[x].append(y)
        graph[y].append(x)
    
    def bfs(v):
        visited = [0 for _ in range(n+1)]
        visited[v] = 1
        q = deque([(v)])
        cnt = 1
        
        while q:
            s = q.popleft()
            for i in graph[s]:
                if visited[i] == 0:
                    cnt += 1
                    visited[i] = 1
                    q.append((i))
                
        return cnt 
    
    res = n
    for x, y in wires:
        graph[x].remove(y)
        graph[y].remove(x)
        
        res = min(abs(bfs(x) - bfs(y)), res)
        
        graph[x].append(y)
        graph[y].append(x)
        
    return res
