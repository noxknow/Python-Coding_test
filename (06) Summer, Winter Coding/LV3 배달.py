from collections import deque

def solution(N, road, K):
    answer = 0
    visited = [1e9] * (N+1)
    visited[1] = 0
    
    graph = [[] for _ in range(N + 1)]
    for a,b,c in road:
        graph[a].append([b,c])
        graph[b].append([a,c])
        
    q = deque([(1,0)])
    
    while q:
        
        target, num = q.popleft()
        
        for j in graph[target]: # 	[[], [[2, 1], [4, 2]], [[1, 1], [3, 3], [5, 2]], [[2, 3], [5, 1]], [[1, 2], [5, 2]], [[2, 2], [3, 1], [4, 2]]]
            if num + j[1] <= K and num + j[1] < visited[j[0]]: # j만 받는 경우 [2, 1], [4, 2], j[1] = 1, 2
                visited[j[0]] = num + j[1]
                q.append([j[0], num + j[1]]) 
                
    for k in visited:
        if k != 1e9:
            answer += 1
    
    return answer
