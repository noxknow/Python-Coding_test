# 방식 1번
n = int(input())
time_list = list(map(int, input().split()))
time_list.sort()

for i in range(1, n):
    time_list[i] += time_list[i-1]
    
print(sum(time_list))

# 방식 2번
n = int(input())
time = list(map(int, input().split()))

time.sort()

result = 0
for i in range(1,n+1):
    result += sum(time[0:i]) # 리스트의 0번째 부터 i-1번째 까지 더해준다.

print(result)

# 방식 3번 (이중 for문이라 시간 복잡도가 크다)
n = int(input())
s = list(map(int, input().split()))

num = 0
s.sort()

for i in range(n): 
    for j in range(i + 1): # 이중 for문 느낌이 약간 1,2,3,4,5 이면 1 + (1+2) + (1+2+3) 이런 느낌
        num += s[j]
print(num)


