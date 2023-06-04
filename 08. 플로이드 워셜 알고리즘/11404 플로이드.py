import sys
sys.stdin=open("input.txt","r")
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(1e9) # 1e9는 실수형이기 때문에 int(1e9) 해준다.
bus_cost = [[INF for _ in range(n+1)] for _ in range(n+1)]

for i in range(m):
    start, end, cost = map(int, input().split())
    bus_cost[start][end] = min(cost, bus_cost[start][end]) # 노선이 하나가 아닐 수 있음 > 최소값 넣기 

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                bus_cost[i][j] = 0
            else:
                bus_cost[i][j] = min(bus_cost[i][j], bus_cost[i][k] + bus_cost[k][j]) 

for i in range(1, n+1):
    for j in range(1, n+1):
        if bus_cost[i][j] == INF:
            print(0, end = " ")
        else:
            print(bus_cost[i][j], end = " ")
    print()
