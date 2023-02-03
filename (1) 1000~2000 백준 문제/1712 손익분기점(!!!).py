# 시간 초과
x, y, z = map(int, input().split())

if z <= y :
    print(-1)
else:
    cnt = 0
    while x + y*cnt >= z*cnt:
        cnt += 1
    print(cnt)

# 정답 코드
A, B, C = map(int, input().split())

if B>=C:
    print(-1)
else:
    print(int(A/(C-B)+1))