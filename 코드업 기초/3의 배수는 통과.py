# 3의 배수는 통과
n = int(input())

for i in range(1,n+1):
    if i%3 == 0:
        continue
    else:
        print(i, end = " ")

# 위처럼 말고 if i%3: print(i, end = " ")로 두줄로도 가능하다. [참 거짓 이용]
n = int(input())

for i in range(1,n+1):
    if i%3:
        print(i, end = " ")

