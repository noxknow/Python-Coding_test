import sys
input = sys.stdin.readline

n,k = map(int, input().split())

num_list = []
for _ in range(n):
    num_list.append(int(input()))

num_list.sort(reverse = True)

result = 0
for i in range(0,n+1):
    if k >= num_list[i]:
        result += k // num_list[i]
        k %= num_list[i]
        if k <= 0:
            break

# for num in num_list: 이렇게도 가능
#     if k >= num:
#         result += k // num
#         k %= num
#         if k <= 0:
#             break
    
print(result)
