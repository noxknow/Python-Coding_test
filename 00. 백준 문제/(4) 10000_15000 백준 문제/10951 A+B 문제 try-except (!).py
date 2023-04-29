# A+B 케이스가 나오는데 0 0이 나오면 출력이 멈추는 경우
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print(a+b)

# 케이스의 개수를 모르기에 에러가 발생하면 빠져나갈 수 있는 try - except 구문
while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break