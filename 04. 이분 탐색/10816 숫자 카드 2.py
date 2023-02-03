# 딕셔너리와 이분탐색의 조화 (솔직히 이상하다 이럴거면 딕셔너리만 쓰는게 맞다)
import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

dic = {}
for i in n_list:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for m in m_list:        
    left = 0
    right = n-1

    while left <= right:
        mid = (left + right) // 2

        if m >= n_list[mid]:
            left = mid + 1
        else:
            right = mid - 1

    if m == n_list[mid]:
        print(dic[m], end = " ")
    else:
        print(0, end = " ")

# 딕셔너리 이용
import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

dic = Counter(n_list) # 이렇게도 표현가능하고, 아래처럼도 가능하다.
# dic = {}
# for i in n_list:
#     if i in dic:
#         dic[i] += 1
#     else:
#         dic[i] = 1

for i in m_list:
    if i in dic:
        print(dic[i], end = " ")
    else:
        print(0, end = " ")

# 내가 하려고 했으면 이렇게 했어야 함
n = int(input())
cards = list(map(int, input().split(' ')))
cards.sort()

m = int(input())
targets = list(map(int, input().split(' ')))

result = list()


def down_binary(target):
    left = 0
    right = len(cards) - 1

    while left <= right:
        mid = (left + right) // 2

        if cards[mid] >= target:
            right = mid - 1
        elif cards[mid] < target:
            left = mid + 1
    return left

def up_binary(target):
    left = 0
    right = len(cards) - 1

    while left <= right:
        mid = (left + right) // 2

        if cards[mid] > target:
            right = mid - 1
        elif cards[mid] <= target:
            left = mid + 1
    return left

for i in range(m):
    print(up_binary(targets[i])-down_binary(targets[i]), end=' ')

# 내가 했지만 안되는 거
import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
n_list.sort()

def board(i):
    left = 0
    right = n-1
    cnt = 0

    while left <= right:
        mid = (left + right) // 2

        if i >= n_list[mid]:
            if mid == n-1 or mid == 0:
                cnt += 1
                break

            if i == n_list[mid] and i == n_list[mid+1]:
                cnt += 1
                left = mid + 1
            elif i == n_list[mid] and i == n_list[mid-1]:
                cnt += 1
                right = mid - 1
            elif i == n_list[mid]:
                cnt += 1
                left = mid + 1
            else:
                left = mid + 1
        else:
            right = mid - 1

    return str(cnt)

result = ""
for i in range(m):
    result += board(m_list[i])

print(" ".join(result))