import heapq
import sys
input = sys.stdin.readline

n = int(input())

cards = []
result = 0

for i in range(n):
    heapq.heappush(cards, int(input())) # 우선순위 큐에 오름차순으로 정리해준다.
if len(cards) == 1:
    print(0)
else:
    while len(cards) > 1:
        print(cards)
        plus = heapq.heappop(cards) + heapq.heappop(cards) # heappop 작은수 부터 꺼내준다.
        result += plus
        heapq.heappush(cards, plus)

    print(result)

# 시간 초과이긴 하지만 다른 방법
import sys
input = sys.stdin.readline

n = int(input())

my_list = []
for i in range(n):
    my_list.append(int(input()))

my_sum = []

while 1 :
    if len(my_list) >= 2 : 
        a = my_list.pop()
        b = my_list.pop()
        my_sum += (a+b)
        my_list.append(a+b)
        my_list = sorted(my_list, reverse = True)
    elif len(my_list) == 1 : 
    	break