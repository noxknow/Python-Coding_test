import sys
input = sys.stdin.readline

n = int(input())

time_list = []
for i in range(n):
    a,b = map(int, input().split())
    time_list.append([a,b])

time_list.sort(key=lambda x: (x[1], x[0]))

last = 0
cnt = 0
for i,j in time_list:
    if i >= last:
        cnt += 1
        last = j
        
print(cnt)