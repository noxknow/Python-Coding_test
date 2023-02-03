# 내가 풀었을 때
a = int(input())
s=0

for i in range(1,a+1):
    if i % 2 == 0:
        s += i
        
print(s)

# 우리밋 식 첫번째
num = int(input())

print('== #1 ==')
answer = 0
for i in range(2, num+1, 2): # 아예 범위를 2씩 증가시켜서 짝수만 더하는 방법
  answer += i
print(answer)

# 우리밋 식 두번째
print('== #2 ==')
answer2 = [i for i in range(2, num+1, 2)] # list comprehension 방식으로 하나로 묶을 수 있다.
print( sum(answer2) )

# 우리밋 식 세번째
print('== #3 ==')
answer3 = range(2, num+1, 2) # range로 리스트 함수로 만들고 sum 해주면 된다.
print( sum(answer3) )