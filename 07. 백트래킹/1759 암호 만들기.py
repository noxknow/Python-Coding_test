import sys
sys.stdin=open("input.txt","r")
input = sys.stdin.readline
 
def dfs(cnt, idx):
    if cnt == n:
        vo, co = 0, 0

        for j in res:
            if j in vowel:
                vo += 1
            else:
                co += 1
        
        if vo>=1 and co>=2:
            print("".join(res))

        return
    
    for i in range(idx, m):
        res.append(word_list[i])
        dfs(cnt+1, i+1)
        res.pop()

n, m = map(int, input().split())
word_list = sorted(list(map(str, input().split())))
vowel = ['a', 'e', 'i', 'o', 'u']
res = []
dfs(0, 0)
