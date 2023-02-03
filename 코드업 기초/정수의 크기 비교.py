# 정수 2개 입력받아 큰 값 출력하기
a,b = input().split()
a = int(a)
b = int(b)
c = (a if (a>=b) else b)

print(int(c))

# 정수 3개 입력받아 짝/홀 출력하기
a,b,c = map(int, input().split())

if a%2 == 0:
    print("even")
else:
    print("odd")

if b%2 == 0:
    print("even")
else:
    print("odd")

if c%2 == 0:
    print("even")
else:
    print("odd")

# 정수 1개 입력받아 분류하기
a = int(input())

if a<0:
    if a%2 == 0:
        print("A")
    else:
        print("B")
elif a>0:
    if a%2 == 0:
        print("C")
    else:
        print("D")

# 점수 평가하기
a=int(input())

if a>=90:
    print("A")
elif a>=70:
    print("B")
elif a>=40:
    print("C")
else:
    print("D")

# 평가 입력받아 다르게 출력하기
a = input()

if a == "A":
    print("best!!!")
elif a == "B":
    print("good!!")
elif a == "C":
    print("run!")
elif a == "D":
    print("slowly~")
else:
    print("what?")