import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
 
a.sort() # b 재배열 말이 없었으면 b는 내림차순으로 배열했으면 그것도 정답이긴했다.
result = 0
for i in range(n):
    x = a[i]
    y = b.pop(b.index(max(b))) # pop은 주어진 인덱스의 값을 리스트에서 삭제하고 돌려주는 역할
    result += x*y

print(result)