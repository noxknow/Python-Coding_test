# 파이썬만 가능
case = int(input())

num_list = []
for i in range(case):
    num_list.append(int(input()))

num_list.sort()

# print(*num_list)

for i in num_list: 
    print(i)

# 버블 정렬
N = int(input())

numbers = []

for _ in range(N) : 
    numbers.append(int(input()))

# Bubble Sort
for i in range(len(numbers)) : 
    for j in range(len(numbers)) : 
        if numbers[i] < numbers[j] : 
            numbers[i], numbers[j] = numbers[j], numbers[i]
            
for n in numbers : 
    print(n)

# 삽입 정렬
N = int(input())
nums = []

for _ in range(N) : 
    nums.append(int(input()))

# Insert Sort
for i in range(1, len(nums)) :
    while (i>0) & (nums[i] < nums[i-1]) :
        nums[i], nums[i-1] = nums[i-1], nums[i]
        
        i -= 1
        
for n in nums : 
    print(n)