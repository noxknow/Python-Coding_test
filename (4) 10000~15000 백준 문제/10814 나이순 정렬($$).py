import sys
input = sys.stdin.readline

n = int(input())

enter = []
for _ in range(n):
    enter.append(input().split())

enter.sort(key=lambda x : int(x[0])) # 나이와 이름중 나이를 오름차순으로 정렬을 의미

for i in enter:
    print(i[0], i[1])