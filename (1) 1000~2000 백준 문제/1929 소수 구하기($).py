# 2581과 다른 방식의 소수 찾기 (하지만 시간 초과)
m, n = map(int, input().split())

arr = [i for i in range(m,n+1)] # 배열에 1부터 자기자신 까지 다 넣는다

for i in arr:
    num=0
    for j in range(1,i+1):
        if i%j==0:
            num+=1
    if num == 2:
        print(i)

# 시간 초과 안걸리는 에라토스테네스의 체
m, n = map(int, input().split())

prime_list = [True]*(n+1) # 리스트를 n+1개 만들고
prime_list[0] = False # 리스트의 0번지와 1번지는 미리 false 해두고
prime_list[1] = False

for i in range(2,int(n**0.5)+1): # n의 제곱근까지만 검사
	if prime_list[i]:
		for j in range(i*2,n+1,i):
			prime_list[j] = False  # prime 내 i의 배수들을 False로 변환

for i in range(m,n+1):
	if prime_list[i]: # 예를 들어 3 16이면 prime리스트 안의 3번지부터 16번지가 TRUE인 값만 출력하라
		print(i)

# 시간초과 다른 예시
m, n = map(int, input().split())

def isPrime(x):         # 소수를 판별하는 함수
  if(x<2):              # 1은 소수가 아니므로 False
    return False
  for i in range(2,x):
    if(x%i==0):	        # 2부터 주어진 수x 사이의 수로 x가 나누어떨어지면 False
      return False
  return True           # 1과 자기자신만으로 나누어 떨어지므로 소수

for i in range(m, n+1): # m부터 n까지 소수를 하나하나 찾음
  if(isPrime(i)):
    print(i)

# 에라토스테네스의 체 다른 예시
m, n = map(int, input().split())

def isprime(m, n):
  n += 1                            # for문 사용을 위한 n += 1
  prime = [True] * n                # n개의 [True]가 있는 리스트 생성
  for i in range(2, int(n**0.5)+1): # n의 제곱근까지만 검사
    if prime[i]:                    # prime[i]가 True일때
      for j in range(2*i, n, i):    # prime 내 i의 배수들을 False로 변환
        prime[j] = False

  for i in range(m, n):
    if i > 1 and prime[i] == True:  # 1 이상이면서 남은 소수들을 출력
      print(i)

isprime(m, n)