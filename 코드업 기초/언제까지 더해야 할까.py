# 언제까지 더해야 할까?
a = int(input())
s = 0

for i in range(1,a+1):
    s += i
    if s >= a:
        break

print(i)

# 더했을 때 그 때 까지의 합을 출력
n = int(input())
s = 0

for i in range(1,n+1):
    s += i 
    if s>=n:
        break
   
print(s)