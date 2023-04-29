from itertools import combinations

def solution(numbers):
    answer = []
    
    combi = list(combinations(numbers,2))
    
    res = 0
    for a,b in combi:
        res = a+b
        if res not in answer:
            answer.append(res)
    
    return sorted(answer)
