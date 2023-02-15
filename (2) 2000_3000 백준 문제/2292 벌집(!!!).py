N = int(input())

first_num = 1
cnt = 1
while N > first_num:
    first_num += 6 * cnt
    cnt += 1

print(cnt)