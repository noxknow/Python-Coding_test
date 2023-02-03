# 등차수열 나열하기(내가 푼 것)
a,d,n = map(int, input().split())
count = 0
s = 0

while True:
    count += 1
    s = a + d*(count-1)
    if count == n:
        break

print(s)

# 등차수열 나열하기(컴퓨터가 푼 것)
a,d,n=input().split()

a=int(a)
d=int(d)
n=int(n)

s=a
for i in range(2, n+1):
   s+=d

print(s)

# 등비수열 나열하기(내가 푼 것)
a,r,n = map(int, input().split())
count = 0
s = 0

while True:
    count += 1
    s = a * r**(count-1)
    if count == n:
        break

print(s)

# 등비수열 나열하기(컴퓨터가 푼 것)
a, r, n = input().split()

a = int(a)
r = int(r)
n = int(n)

for i in range(1, n) :
  a = a*r

print(a) 

# 등차 + 등비 수열 나열하기(내가 푼 것) -> 시간이 오래걸림 코드가 안좋은듯
a,r,d,n = map(int, input().split())
count = 0

while True:
    count += 1
    a = a * r + d
    if count == n-1:
        break

print(a)  

# 등차 + 등비 수열 나열하기(컴퓨터가 푼 것)
a,r,d,n = map(int, input().split())

for i in range(1,n):
    a = a*r+d
    
print(a)
