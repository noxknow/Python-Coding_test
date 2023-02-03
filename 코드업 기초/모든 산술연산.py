a,b = input().split()

n1 = int(a) + int(b)
n2 = int(a) - int(b)
n3 = int(a) * int(b)
n4 = int(a) // int(b) # 몫
n5 = int(a) % int(b) # 나머지
n6 = int(a) / int(b) # 나눈 값
n7 = int(a) ** int(b) # 거듭제곱

print(n1)
print(n2)
print(n3)
print(n4)
print(n5)
print(format(n6,".2f"))
print(n7)

# 정수 3개 입력받아 합과 평균 출력하기
a,b,c = input().split()
n1 = int(a) + int(b) + int(c)
n2 = (int(a) + int(b) + int(c)) / 3

print(n1, format(n2,".2f"))

# 정수 3개 입력받아 합과 평균 출력하기 (map을 이용하여 정수형으로 치환)
a,b,c = map(int, input().split())

n1 = a + b + c
n2 = (a + b + c) / 3

print(n1, format(n2,".2f"))
