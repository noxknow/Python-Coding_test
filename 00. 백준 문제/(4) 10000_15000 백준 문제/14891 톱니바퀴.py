import sys
from collections import deque
sys.stdin=open("input.txt","r")
input = sys.stdin.readline

def cal_left(idx, check, direction):
    # 비교할 톱니바퀴의 인덱스가 0 이라는 것은 제일 왼쪽에 위치한다는 의미이므로 비교할 필요 없음
    if idx == 0:
        return

	# 현재 톱니바퀴와 그 왼쪽으로 위치한 톱니바퀴의 맞닿는 극 체크 
    if gear[idx][6] != gear[check][2]:
        # 함수가 시작하기 전에 본체의 방향은 이미 저장했으니 왼쪽과 극이 다르다면 
        # 왼쪽 톱니는 반대방향으로 회전한다. 즉, dir * -1을 해줘야 한다.
        need_rotate.append((check, direction * (-1)))
        # 계속해서 왼쪽 방향 체크
        cal_left(idx - 1, check - 1, direction * (-1))

def cal_right(idx, check, direction):
    if idx == 3:
        return
        
    if gear[idx][2] != gear[check][6]:
        need_rotate.append((check, direction * (-1)))
        cal_right(idx + 1, check + 1, direction * (-1))

gear = [deque(map(int, input().rstrip())) for _ in range(4)]
t = int(input())

for _ in range(t):
    need_rotate = []
    start, dir = map(int, input().split())
    need_rotate.append((start - 1, dir))

    cal_left(start - 1, start - 2, dir)
    cal_right(start - 1, start, dir)

	# 톱니바퀴 회전
    for idx, direction in need_rotate:
        gear[idx].rotate(direction)

ans = 0
res = 1
for i in range(4):
    if gear[i][0] == 1:
        ans += res
    res *= 2
print(ans)
