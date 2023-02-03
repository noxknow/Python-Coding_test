import sys
input = sys.stdin.readline

a, b = map(int,input().split())

count = 1
while True:
    if a == b:
        break
    elif a>b:
        count=-1
        break
    elif b%10 == 1: # 난 이걸 리스트로 만들어서 pop을 통해 1을 빼줄 생각 이였는데 불가능.
        b//=10
        count+=1
    elif b%2 == 0:
        b//=2
        count+=1
    else:
        count=-1
        break
print(count)

"""
리스트 보다 데크가 pop 연산 같은곳에서 훨씬 우월한 타입이다.
"""
from collections import deque

a, b = map(int,input().split())
result = -1
q = deque([(a,1)])

while q:
    i, cnt = q.popleft()
    if i == b:
        result = cnt
        break
    
    if i*2 <= b:
        q.append((i*2, cnt+1))
    if int(str(i) + "1") <= b:
        q.append((int((str(i) + "1")), cnt+1))

print(result)