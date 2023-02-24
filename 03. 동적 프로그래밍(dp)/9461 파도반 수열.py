t = int(input())

p = [0] * 101
p[0] = 1
p[1] = 1
p[2] = 1

for j in range(98):
    p[j+3] = p[j] + p[j+1]

for i in range(t):
    n = int(input())
    
    print(p[n-1])
