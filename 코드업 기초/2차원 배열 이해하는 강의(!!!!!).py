import numpy as np
cur = tuple(map(int, input().split()))
left, right, up, down = map(int, input().split())

# coords = [[0 for _ in range(5)] for _ in range(5)]
coords = np.zeros((5, 5), dtype = int)
move = (cur[0]-up+down, cur[1]-left+right)
coords[move[0]-1][move[1]-1] = 1

"""
print(*coords) 이렇게만 하면 언패킹만 되고 아래처럼 crd라는 변수를 하나 만들어서
다시 넣어줘야 원하는 형태로 나오게 된다.
for i in range(5):           -> 밑의 프린트 방법하고 이것 둘중 하나 사용
    print(*coords[i])
"""
for crd in coords: 
    print(*crd)