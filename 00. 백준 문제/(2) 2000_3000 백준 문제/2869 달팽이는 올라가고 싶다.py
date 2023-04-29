# 정상에 도착해도 내려와 버려서 안됨
A, B, V = map(int, input().split())

day = 1
h = 0
while h <= V:
    h = (A-B) * day
    day += 1

print(day)

# 이렇게 풀면 시간 초과
A, B, V = map(int, input().split())

day = 0
h = 0
while True:
    day += 1
    h += A
    if h >= V :
        print(day)
        break
    h -= B

# 이렇게 푼다
import math

a, b, v = map(int, input().split())
# a= 올라가는 길이, b= 떨어지는길이, v= 나무높이 

day = math.ceil((v-a)/(a-b)) + 1
print(day)

# 좀 특이한거 풀리긴 한다
A, B, V = map(int, input().split())

high = V - A
if high % (A-B) == 0:
    first = int(high/(A-B))
else:
    first = int(high/(A-B) + 1)
print(first + 1)