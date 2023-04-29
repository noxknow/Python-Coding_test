n,l = map(int, input().split())
s = list(map(int, input().split()))

s.sort()

start = s[0]
cnt = 1

for i in s[1:]:
  if i in range(start, start+l):
    continue
  else:
    start = i
    cnt += 1
    
print(cnt)
