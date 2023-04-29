import sys
input = sys.stdin.readline
from collections import Counter
n = int(input())

num_list = []
for _ in range(n):
    num_list.append(int(input()))
    
num_list.sort()
nums_s = Counter(num_list).most_common()

result1 = sum(num_list) / n
print(round(result1))
print(num_list[n//2])
if len(nums_s) > 1:
    if nums_s[0][1] == nums_s[1][1]:  
        print(nums_s[1][0])
    else:
        print(nums_s[0][0])
else:
    print(nums_s[0][0])
print(num_list[-1] - num_list[0])

"""
counter().most_common()의 함수가 가장 빈도가 많은 작은수를 왼쪽 부터 시작 하게 되는데
[(-1,2), (-2,2), (-3,1)]의 경우 nums_s[0][1]는 -1의 빈도인 2를 의미하고, nums_s[1][1]
는 -2의 빈도인 2를 의미한다. nums_s[2][0] = -3 일것이고, nums_s[2][1] = 1을 의미한다.
"""