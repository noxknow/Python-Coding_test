import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
m = int(input())

low, high = 0, max(s)
while low <= high:
    mid = (low + high) // 2
    num = 0
    for i in s:
        if i >= mid: num += mid
        else: num += i
    if num <= m: low = mid + 1
    else: high = mid - 1
print(high)
