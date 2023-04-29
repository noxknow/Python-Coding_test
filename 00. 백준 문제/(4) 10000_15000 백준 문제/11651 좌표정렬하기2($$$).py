import sys
input = sys.stdin.readline

n = int(input())

coor = []
for _ in range(n):
    [a,b] = list(map(int, input().split()))
    coor.append([b, a])

coor.sort() # b = sorted(coor) 로도 정렬 가능

for i in range(n):
    print(coor[i][1], coor[i][0])

# key = lambda 이용
import sys
input=sys.stdin.readline

N = int(input()) # 점의 갯수

num = []

# 리스트에 좌표 입력
for _ in range(N) :
    a,b = map(int, input().split())
    num.append([a,b])

# y좌표로 정렬 후에, 다시 x좌표로 정렬
num.sort(key = lambda x : (x[1], x[0]))

# 출력
for i in num :
    print(i[0], i[1]) # [2, 3] 의 경우 2 3 이런식으로 출력 해줌

"""
key=lambda x : (x[1], x[0]) 에서 앞의 x[1]의 의미 (a,b)의 1번째 인덱스를 기준으로
오름차순 정렬 한 후, x[0] (a,b)의 0번째 인덱스를 기준으로 오름차순 정렬 하겠다.
만약 -x[0]의 경우 0번째 인덱스를 내림차순 하겠다는 의미.

c = sorted(num, key=lambda x : (x[1], x[0])) --> sorted 함수 사용하는 경우
"""
