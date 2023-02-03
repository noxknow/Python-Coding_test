import sys
input = sys.stdin.readline

n = int(input())
n_arr = list(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))
n_arr.sort()

def binary(i):
    left = 0
    right = n-1

    while left <= right:
        mid = (left + right) // 2

        if i == n_arr[mid]:
            return True
        
        if i > n_arr[mid]:
            left = mid + 1
        else: 
            right = mid - 1

    return False
        
for i in range(m):
    if binary(m_arr[i]):
        print(1)
    else:
        print(0)
        
"""
이분 탐색에서 right 값을 n-1로 쓰냐 max()로 쓰냐 의 차이는 예를 들어

4 1 5 2 3 숫자는 여러개지만 이 모든 숫자가 하나의 배열로 생각해서 그 하나 안에서 처리하기 때문에 
right이 n-1이고

20 15 10 17 일때는 숫자가 여러개지만 각 길이마다 배열이 생기므로 총 4개의 배열로 봐야 하므로,  
right을 max() 형식으로 써야한다.
"""
    
            
            


                
