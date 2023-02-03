# 바둑판에 흰 돌 놓기
import numpy as np
n = int(input())
shape = np.zeros((19,19), dtype = int) # shape = [[0 for _ in range(19)] for _ in range(19)]

for _ in range(n):
    x,y = map(int, input().split()) 
    shape[x-1][y-1] = 1
"""
x,y = map(lambda num : int(num)-1, input().split()) 해주면 x-1을 해줄 필요가 없다. 
실무에서 더 유용하게 사용하는 함수이다. (lambda)
"""
for s in shape:
    print(*s)


