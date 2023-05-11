h = []
for i in range(9):
    h.append(int(input()))

sum_ = sum(h)
h.sort()
start = 0
end = 8
while True:
    if h[start] + h[end] < sum_ - 100:
        start += 1
    elif h[start] + h[end] > sum_ - 100:
        end -= 1
    else:
        break
    
for i in range(9):
    if i != start and i != end:
        print(h[i])
