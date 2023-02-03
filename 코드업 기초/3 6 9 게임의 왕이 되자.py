# 3 6 9 게임의 왕이 되자

n = int(input())

for i in range(1,n+1):
    if i%10==3 or i%10==6 or i%10==9:
        print("X", end = " ")
    else:
        print(i, end = " ")

# 우리밋 식
num = int(input())

for i in range(1, num+1):
  count = i if i%3 else 'X'
  print(count, end=' ')