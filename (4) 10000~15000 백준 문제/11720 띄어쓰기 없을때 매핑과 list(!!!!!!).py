# 내가 풀었지만 너무 길다
number = int(input())
num_list = int(input())

answer = 0
for num in str(num_list):
    answer += int(num)
    
print(answer)

# 띄어쓰기로 대입을 안할때 list를 활용할 수 있는 방법 찾음
number = int(input())
num_list = list(map(int, input()))
print(sum(num_list))