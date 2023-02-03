import sys
input = sys.stdin.readline

cnt = 0
i = 0
while True:
    [a, b, c] = map(int, input().split())
    if [a, b, c] == [0, 0, 0]:
        break 
    cnt = c // b
    s = c % b
    if a < s: # 예를 들어 5 7 20 인 경우 나머지만 생각하면 5+5+6 이지만 이럼 안되고 5+5+5가 맞음.
        s = a
    result = (a * cnt) + s
    i += 1
    print(f'Case {i}: {result}')