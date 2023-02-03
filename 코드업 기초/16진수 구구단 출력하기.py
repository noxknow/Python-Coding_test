# 16진수 구구단 출력하기(컴퓨터)

# 또는
# print("%X*%X=%X"%(n,i,n*i))
n = int(input(), 16)

for i in range(1, 16) :
  print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')

# 16진수 구구단 출력하기(내가 한것)
a = input()
n = int(a, 16)

for i in range(1,16):
    print('%X'%n, '*%X'%i, '=%X'%(n*i), sep = "")

# 16진수로 변환해주는 함수 hex, hex(i)[2:].upper() 
# -> i를 hex로 16진수로 변환하고 0x1 이런식으로 나오면 2번째인 1만 나오도록 해주고 upper이용해서 대문자로 바꿔주기


