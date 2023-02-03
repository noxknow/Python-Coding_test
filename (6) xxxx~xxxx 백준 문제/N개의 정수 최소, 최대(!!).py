# 내가 한거 (이때 N 범위가 1000000까지라 너무커서 시간이 오래걸림)
N = int(input())
A = list(map(int, input().split()))

print(min(A), max(A))

# 정렬 방식으로 다르게 푼 것
n = int(input())
lis = list(map(int, input().split()))
lis.sort()
print(lis[0],lis[n-1])

# 시간을 줄여보려 했지만 줄지 않음
import sys
input = sys.stdin.readline

n = int(input())
lis = list(map(int, input().split()))
lis.sort()
print(lis[0],lis[n-1])


