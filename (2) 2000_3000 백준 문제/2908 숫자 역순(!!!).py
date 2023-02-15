# 내가 푼 것
x, y = input().split()
re_x = 1*int(x[0]) + 10*int(x[1]) + 100*int(x[2])
re_y = 1*int(y[0]) + 10*int(y[1]) + 100*int(y[2])

print(max(re_x, re_y))

# 남이 푼 것
num1, num2 = input().split()
num1 = int(num1[::-1])  # [::-1] : 역순
num2 = int(num2[::-1])

print(max(num1, num2))
