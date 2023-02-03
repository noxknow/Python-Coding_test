import heapq

def solution(food_times, k):
    if sum(food_times) <= k: # 전체 음식을 먹는 시간보다 k가 크거나 같으면 -1
        return -1
    
    q = [] 
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1)) # (음식시간, 음식번호)를 우선순위 큐에 삽입
        
    sum_value = 0 #  먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    length = len(food_times) # 남은 음식의 개수
    
    # "먹기 위해 사용한 시간 + (현재 음식 시간 - 이전 음식 시간) * 현재 남은 음식 개수" 와 "k" 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0] # 현재 음식 시간
        sum_value += (now - previous) * length 
        length -= 1 # 다 먹은 음식 제외
        previous = now # 이전 음식을 현재 음식으로
        
    result = sorted(q, key = lambda x: x[1]) # 음식 번호 기준으로 정렬하여 저장
    
    return result[(k - sum_value) % length][1]
    
food_times = [3, 1, 2]
k = 5
solution(food_times, k)

"""
1번 음식: 8초 소요
2번 음식: 6초 소요
3번 음식: 4초 소요
k = 15
이 경우에 우선순위 큐에 값을 삽입하면 q = [(4,3), (6,2), (8,1)] 이 되고, length = 3 이 된다.

while문이 어떻게 진행되는지 보면,
# 1 

먹기 위해 사용한 시간(0) + ((현재 음식 시간(4) - 이전 음식 시간(0)) * 남은 음식 개수(3)) <= 15 
-> 12 <= 15 가 성립하므로 현재 음식을 뺄 수 있다. 그러면 now = 4, 
sum_value = *(4 - 0) * 3 = 12, length = 3 - 1 = 2, previous = 4 가 된다.

# 2

먹기 위해 사용한 시간(12) + ((현재 음식 시간(6) - 이전 음식 시간(4)) * 남은 음식 개수(2)) <= 15 
-> 16 <= 15 가 성립하지 않으므로 while문을 빠져나온다.

result = [(8,1), (6,2)] 가 되고, result[(15 - 12) % 2][1] = result[1][1] = 2가 리턴된다.
"""