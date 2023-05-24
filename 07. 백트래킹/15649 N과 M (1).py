import sys
sys.stdin=open("input.txt","r")
input = sys.stdin.readline

def dfs(num, lst):
    if num==m:
        ans.append(lst)
        return
    
    for j in range(1, n+1):
        if visited[j] == 0:
            visited[j] = 1
            dfs(num+1, lst+[j])
            visited[j] = 0

n, m = map(int, input().split())
ans = []
visited = [0] * (n+1)

dfs(0, [])
for lst in ans:
    print(*lst)
