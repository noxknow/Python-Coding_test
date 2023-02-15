# int형으로 풀기
N = int(input())  #입력받은 값을 int로 바꿈
num = N           #변하는 값
count = 0         #몇 번 사이클인지
 
while True:
    a = num//10
    b = num %10
    c = (a+b)%10
    num = (b*10) + c
    count += 1
    if(num == N):
        break
 
print(count)

# str형으로 풀기 (시간초과로 잘 안되긴하지만 알아두기)
N = input()
num = N           
count = 0  

while True:
    if len(num) == 1:
        num = "0" + num
    plus = str(int(num[0]) + int(num[1]))
    num = num[-1] + plus[-1]
    count += 1
    if num == N:
        print(count)
        break

