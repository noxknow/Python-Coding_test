T = int(input())

for x in range(T):
    H, W, N = map(int, input().split())
    floor = N%H
    num = N//H + 1
    if N%H == 0:
        floor = H
        num = N//H
    print(floor*100 + num)