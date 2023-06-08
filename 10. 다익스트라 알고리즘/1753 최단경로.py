import sys
import heapq
sys.stdin=open("input.txt","r")
input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())
INF = int(1e9)
dp = [INF] * (v+1)
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dp[start] = 0

    while q:
        dist, node = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if dp[node] < dist:
            continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for next_node, next_dist in graph[node]:
            cost = dist + next_dist
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우 (첫번째 경우 dp값이 INF니깐 성립)
            if cost < dp[next_node]:
                dp[next_node] = cost
                heapq.heappush(q, (cost, next_node))

dijkstra(k)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, v+1):
    if dp[i] == INF:
        print("INF")
    else:
        print(dp[i])

