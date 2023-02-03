# 정확성은 맞지만 효율이 안좋다.
def solution(stones, k):
    answer = 0
    while True:
        answer += 1
        for i in range(len(stones)):
            if stones[i] == 0:
                continue
            else:
                stones[i] -= 1
            
        cnt = 0
        
        for stone in stones:
            if stone == 0:
                cnt += 1
                if cnt == k:
                    return answer
            else:
                  cnt = 0 # 초기화의 의미를 갖고있다. 위에서 0이 연속적으로 안나오고 0 0 4 이런식으로 나오면 4에서 cnt를 다시 0으로 초기화

# 이분 탐색 방법 (효율이 좋다.)
def solution(stones, k):
    left = 0
    right = max(stones)
    while left <= right:
        mid = (left + right) // 2 # (현재 생각하는 건널 수 있는 사람 수)
        cnt = 0

        for stone in stones:
            if stone - mid <= 0: 
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                # answer = mid
                break
        if cnt >= k: # 최대cnt가 k보다 크거나 같다면, 건너는 사람 수는 더 작아져야 하므로, end를 mid-1로 줄여준다.
            answer = mid # 위 혹은 여기, 아래는 틀리다 (왜냐, cnt == k 일때의 마지막 값이 이 때 저장되기 때문에)
            right = mid - 1
        else: # 최대cnt가 k보다 작다면, 건너는 사람 수는 더 커져야 하므로, start를 mid+1로 늘려준다.
            left = mid + 1

    return answer # print(left) 혹은 answer = left, print(answer), answer = mid 위치는 while문 나갈 때를 잘 생각해서 최대 일 때 써줘야함 

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
print(solution(stones, 3))


"""
이 문제를 보고 이분탐색이라고 판단해야 하는이유.

1. 우선 범위가 2억이므로 매우크다 -> 이분탐색을 떠올린다!
2. 어떤 조건을 만족하는 인원수의 최대값을 구해야한다 -> 최적화문제 -> 파라메트릭서치를 이용한다. 
(어떤 조건에 부합하는 가능한 최대, 혹은 최소 등과같은 문제)
3. 여기서는 k가 주어질때 이 k의 조건을 만족하는 인원수의 최대이므로 인원수를 기준으로 이분탐색을 진행한다.

mid명이 징검다리를 건넌다고 할때 가능한가? 에 대한 가설을 검증

1. mid명이 징검다리를 건널때 돌의 상태를 계속 체크하는데 앞에서부터 가다가 연속된 0이 k만큼 최초로 
나온경우, 현재 mid명수의 사람은 건널수 없음을 의미하므로 right = mid-1를 통해 인원수를 줄여준다.
2. 만약 mid명이 징검다리를 건넜는데 연속된 0의 돌이 k미만이다? 현재의 인원수는 건너는게 가능하군!
인원수를 늘려줘본다.

answer = mid # 위 혹은 여기, 아래는 틀리다 (왜냐, cnt == k 일때의 마지막 값이 이 때 저장되기 때문에)
cnt<k 라면 else 로 빠지고 이때의 값은 answer에 저장할 필요가 없기 때문에 cnk >= k 일 때만
"""
