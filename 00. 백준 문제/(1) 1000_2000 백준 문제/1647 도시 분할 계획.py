import sys
sys.stdin=open("input.txt","r")
input = sys.stdin.readline

def find(p):
    if p == parent[p]:
        return p

    parent[p] = find(parent[p])
    return parent[p]

def union(x, y):
    x = find(x)
    y = find(y)

    if y < x:
        parent[x] = y
    else:
        parent[y] = x

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
graph.sort(key=lambda x : x[2])
parent = [i for i in range(n+1)]
ans = []
for a, b, c in graph:
    if find(a) != find(b):
        union(a, b)
        ans.append(c)

print(sum(ans) - max(ans))
