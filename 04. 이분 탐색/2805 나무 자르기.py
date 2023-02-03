import sys
input = sys.stdin.readline

n,m = map(int, input().split())
tree = list(map(int, input().split()))
tree.sort()

def board(m):
    left = 0
    right = max(tree)

    while left <= right:
        mid = (left + right) // 2
        answer = 0

        for num in tree:
            if num >= mid:
                answer += num - mid
        
        if answer >= m:
            result = mid # result = mid 쓰는 위치 잘 생각해야한다. 
            left = mid + 1
        else:
            right = mid - 1
    
    return print(result)

board(m)

"""
4 7               ->  mid 값이 이렇게 변하는데 이 중 15의 위치에 있을 때 result = mid가 마지막으로              
20 15 10 17           저장되고, 18과 16일 때는 else를 따라서 반복하는 중이다.
10
15
18
16
"""

