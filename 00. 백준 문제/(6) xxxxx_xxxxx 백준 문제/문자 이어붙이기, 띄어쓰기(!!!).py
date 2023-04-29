# 내가 한 것
N = int(input())

for i in range(1,N+1):
    A,B = map(int,input().split())
    print("Case #"+str(i)+":",A+B)

# 내가 한 것 고친버젼
N = int(input())

for i in range(1,N+1):
    A,B = map(int,input().split())
    print("Case #%d: %d" %(i, A+B))

# 다른사람이 한 것1
n = int(input())
for i in range(1,n+1):
    print(f'Case #{i}: {sum(map(int,input().split()))}') # 문자열 포매팅 방법

# 다른사람이 한 것2
n = int(input())
for i in range(n):
    print("Case #%d: %d" %(i+1, sum(map(int, input().split()))))
