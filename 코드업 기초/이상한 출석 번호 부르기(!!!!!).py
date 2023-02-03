# 이상한 출석 번호 부르기 (출석 번호를 n번 무작위로 불렀을 때, 각 번호(1 ~ 23)가 불린 횟수)
n = int(input())     #개수를 입력받아 n에 정수로 저장
a = input().split()  #공백을 기준으로 잘라 a에 순서대로 저장

for i in range(n) :  #0부터 n-1까지...
  a[i] = int(a[i])   #a에 순서대로 저장되어있는 각 값을 정수로 변환해 다시 저장

d = []                #d라는 이름의 빈 리스트 [ ] 변수를 만듦. 대괄호 기호 [  ] 를 사용한다.
for i in range(24) :  #[0, 0, 0, ... , 0, 0, 0] 과 같이 24개의 정수 값 0을 추가해 넣음
  d.append(0)         #각 값은 d[0], d[1], ..., d[23] 으로 값을 읽고 저장할 수 있음.

for i in range(n) :    #번호를 부를 때마다, 그 번호에 대한 카운트 1씩 증가
  d[a[i]] += 1

for i in range(1, 24) :  #카운트한 값을 공백을 두고 출력
  print(d[i], end=' ')

# 유튜브 버젼 (출석 번호를 n번 무작위로 불렀을 때, 각 번호(1 ~ 23)가 불린 횟수)***
n = int(input())     
a = map(int,input().split())
student = [0 for _ in range(23)]

for r in a:
    student[r-1] += 1

print( *student ) # *을 이용한 언패킹

# 이상한 출석 번호 부르기 (거꾸로)
n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])

for i in range(n):
    print(a[n-i-1], end = " ")

# 유튜브 버젼 (거꾸로)
n = int(input())     
a = list(map(int,input().split()))
a.reverse()
print(*a)

# 유튜브 버젼 (가장 작은 수)
n = int(input())     
a = map(int,input().split())
print(min(a))
