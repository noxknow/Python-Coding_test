import sys
input = sys.stdin.readline

t = int(input())

def sol(n):
    zeros = [1,0,1] # 0의 경우 숫자가 0,1,2 일때 1번 0번 1번 나온다. 그 이후는 피보나치
    ones = [0,1,1] # 1도 똑같이 그 이후는 피보나치
    if n >= 3:
        for i in range(2,n):
            zeros.append(zeros[i-1] + zeros[i]) # n이 3이라면 zeros = [1,0,1,1] 즉, zeros[3] = 1
            ones.append(ones[i-1] + ones[i]) # n이 3이라면 ones = [0,1,1,2] 즉, ones[3] = 2
    print(zeros[n], ones[n])

for _ in range(t):
    n = int(input())
    sol(n)

# 시도는 좋은데 시간초과
import sys
input = sys.stdin.readline

t = int(input())

cnt0 = 0
cnt1 = 0

def sol(n):
    global cnt0
    global cnt1

    if n == 0:
        cnt0 += 1
        return 0 # 여기서 return값의 의미는 print(sol(0))을 하면 0이 나온다는 소리다
    elif n == 1:
        cnt1 += 1
        return 1 # 즉, print 할 것이 cnt인 우리로써는 return이 0,1,2,3~ 뭐가되든 상관 없다.
    else:
        return sol(n-1) + sol(n-2)

for _ in range(t):
    n = int(input())
    sol(n)
    print(cnt0, cnt1)
    cnt0 = 0
    cnt1 = 0