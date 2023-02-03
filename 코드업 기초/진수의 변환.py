# 10진수를 16진수로
a = int(input())

print('%x'%a)

# 16진수를 8진수로
a = input()
n = int(a, 16)

print('%o'%n)

# 문자를 10진수로
n = ord(input())

print(n)

# 문자 한개 입력받아 다음 문자 출력하기
a = ord(input())

print(chr(a+1))

# 정수 입력받아 문자로 변환하기
c = int(input())

print(chr(c))


