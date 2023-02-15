N = int(input())
num = map(int, input().split())

cnt = 0
for x in num:
    error = 0
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                error += 1
        if error == 0 :
            cnt += 1
print(cnt)