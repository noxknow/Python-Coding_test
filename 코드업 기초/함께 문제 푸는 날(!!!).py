# 함께 문제 푸는 날(유튜브 참조)
a,b,c = map(int, input().split())
d = 0

while True:
    d += 1
    if d%a == 0 and d%b ==0 and d%c ==0: # d 즉, day가 모든 값으로 나눠떨어질 때
        break

print(d)