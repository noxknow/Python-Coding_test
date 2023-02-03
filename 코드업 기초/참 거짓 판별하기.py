# 정수 입력받아 참 거짓 평가하기
a = int(input())

print(bool(a))

# 참 거짓 바꾸기
a = bool(int(input()))

print(not a)

# 둘 다 참일 경우만 참 출력하기 (AND)
a,b = input().split()

print(bool(int(a)) & bool(int(b)))

# 하나라도 참이면 참 출력하기 (OR)
a,b = input().split()

print(bool(int(a)) | bool(int(b)))

# 거짓이 서로 다를 때에만 참 출력하기 (XOR)
a,b = input().split()

print(bool(int(a)) ^ bool(int(b)))

# 참/거짓이 서로 같을 때에만 참 출력하기 (0 0 일때도 true가 나와야함) 1번째 버젼
a,b = input().split()
c = bool(int(a))
d = bool(int(b))

print(((not c) & (not d)) | (c & d))

# 참/거짓이 서로 같을 때에만 참 출력하기 (0 0 일때도 true가 나와야함) 위에거 2번째 버젼
a, b = input().split()
a = bool(int(a))
b = bool(int(b))

print(a==b)