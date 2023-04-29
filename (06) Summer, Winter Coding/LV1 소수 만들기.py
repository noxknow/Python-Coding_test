from itertools import combinations

def solution(nums):
    combi = list(combinations(sorted(nums), 3))
    
    answer = 0
    for tmp in combi:
        if sum(tmp) < 2:
            continue
        sosu = True
        for i in range(2, int(sum(tmp)**0.5)+1):
            if sum(tmp) % i == 0:
                sosu = False
                break
        if sosu:
            answer += 1
    
    return answer
