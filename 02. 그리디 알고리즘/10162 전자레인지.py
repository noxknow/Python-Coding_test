import sys
input = sys.stdin.readline

t = int(input())
time_list = [300, 60, 10]

cnt = 0
result = []

if t % 10 != 0 :
    print(-1)

else:
    for i in time_list:
        cnt = t // i
        t %= i
        result.append(cnt)
    print(result[0], result[1], result[2], sep = " ")

# 다른 버젼
n = int(input())

if n%10 != 0:
	print(-1)
else:
	for i in [300, 60, 10]:
		print(n//i, end=' ')
		n = n%i
