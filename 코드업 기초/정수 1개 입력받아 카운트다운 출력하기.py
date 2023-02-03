# 내가 짠거 카운트다운1
while True:
    a = int(input())
    if a <= a:
        for i in range(1, a+1):
            print(a-i+1) 

# 다른사람이 짠거 카운트다운1 (효율이 더 좋은듯?)
a=int(input())

while a!=0:
    print(a)
    a=a-1

# 내가 짠거 카운트다운2
while True:
    a = int(input())
    if a <= a:
        for i in range(1, a+1):
            print(a-i) 

# 다른사람이 짠거 카운트다운2
a=int(input())

while a!=0:
    a=a-1
    print(a)

# 정수 1개 입력받아 그 수까지 출력하기
n=int(input())

i=0
while i<=n:
    print(i)
    i+=1

# 정수 1개 입력받아 그 수까지 출력하기 (내가 한거)
while True:
    a = int(input())
    for i in range(1,a+2):
        print(i-1)

# 정수 1개 입력받아 그 수까지 출력하기 (더 좋은거)
n=int(input())

for i in range(n+1):
    print(i)

    