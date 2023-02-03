# 설탕과자 뽑기 (혼자 해봤는데 잘 했다.)
h,w = map(int, input().split())
shape = [[0 for _ in range(w)] for _ in range(h)]
"""
만약 numpy로 하는경우
import numpy as np
w, h = map((int, input().split())
shape = np.zeros((w,h), dtype = int)
"""
n = int(input())

for _ in range(n):
    l,d,x,y = map(lambda num : int(num)-1, input().split())
    if d == 0:
        for i in range(l+1):
            shape[x][y+i] = 1 
    else:
        for j in range(l+1):
            shape[x+j][y] = 1 

for s in shape:
    print(*s)


