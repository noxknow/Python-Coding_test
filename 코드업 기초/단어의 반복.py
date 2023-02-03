# 단어 여러번 (split()은 공백을 기준으로)
w,n = input().split()

print(w*int(n))

# 문장 여러번
n = input()
w = input()

print(w*int(n))

# 단어 한개를 나눠서 출력
s=input()

print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

# 단어 이어 붙이기 1
a,b=input().split(" ")

print(a,b,sep="")

# 단어 이어 붙이기 2
a, b = input().split()
print(a+b)



