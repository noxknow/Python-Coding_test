# 주사위 2개 던지기
a,b = map(int, input().split())

for i in range(1,a+1):
    for j in range(1,b+1):
        print(i,j)

# 만약 이걸 list comprehension으로 푼다면 더 복잡해지지만 예시
array = [[(a,b) for b in range(1, b+1)] for a in range(1, a+1)]

for arr in array:
    for r in arr:
        print(*r)
