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

n = int(input())
m = int(input())
graph = [list(map(int, input().split())) for _ in range(m)]
graph.sort(key=lambda x : x[2])
parent = [i for i in range(n+1)]
answer = 0
print(graph)
for a, b, c in graph:
    if find(a) != find(b):
        print(a, b)
        print(parent)
        union(a, b)
        print(parent)
        answer += c

print(answer)
