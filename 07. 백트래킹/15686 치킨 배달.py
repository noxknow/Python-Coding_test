from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
result = 999999
house = []      
chick = []      

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chick.append([i, j])

for chi in combinations(chick, m): 
    temp = 0           
    for h in house: 
        chi_len = 999   
        for j in range(m):
            chi_len = min(chi_len, abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))
        temp += chi_len
    result = min(result, temp)

print(result)
