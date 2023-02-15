import sys
input = sys.stdin.readline

n = int(input())
coor = list(map(int, input().split()))

coors = list(set(coor))
coors.sort()

coordict = {} # 딕셔너리 형태로 만들어야 한다.
for i in range(len(coors)):
    coordict[coors[i]] = i

for i in coor:
    print(coordict[i], end = " ")

"""
딕셔너리는 대칭성을 띄고 있다. 이 문제에서는 {-10 : 0, -9 : 1, 2 : 2, 4 : 3}이 되고
마지막 for문에서 예를 들어 coordict[-9]라고 하면 1이 나오는 것이다.
"""