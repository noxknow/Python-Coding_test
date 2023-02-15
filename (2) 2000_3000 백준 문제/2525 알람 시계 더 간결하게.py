# 내가
H,M = map(int, input().split())

if M - 45 < 0:
    if H == 0:
        print(23, 15+M)
    else:
        print(H-1, 15+M)
else:
    print(H, M-45)

# 다른사람
H,M=map(int,input().split())

if M>=45 : print(H,M-45)
else : print((H+23)%24,M+15)

# 다른사람(코드길이 제일 짧음)
H,M = map(int, input().split())
print((H-(M<45))%24,(M-45)%60) # M<45를 프린트 할 때 나오는 0과1을 이용함

# 다른 알람 시간 (내가 한거)
A,B = map(int, input().split())
C = int(input())

print ((A+((B+C)//60))%24, (B+C)%60)

# 다른 알람 시간 (다른 사람이 한거)
h, m = map(int, input().split())
t = int(input())
x = h*60+m+t
print(x//60%24, x%60)