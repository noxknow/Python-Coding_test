from itertools import combinations_with_replacement as cr

def solution(n, info):
    answer = [-1]
    max_gap = -1
    
    for combi in cr(range(11),n):
        info2 = [0] * 11

        for i in combi:
            info2[10-i] += 1
        
        apeach, lion = 0, 0
        for idx in range(11):
            if info[idx] == info2[idx] == 0:
                continue
            elif info[idx] >= info2[idx]: # info[0]는 10점을 몇번 맞췄는지
                apeach += 10 - idx
            else:
                lion += 10 - idx
        
        if lion > apeach:
            gap = lion - apeach
            if gap > max_gap: #
                max_gap = gap
                answer = info2

    return answer

n = 5
info = [2,1,1,1,0,0,0,0,0,0,0]
print(solution(n, info))

"""
중복조합이 가장 낮은 상태부터 시작하게 되고, 이때 가장 큰 점수차가 여러개여도
gap > max_gap 에서 >= 아니라 > 이기 때문에, 같은 부분이 포함이 안되고 제일 낮았던
점수만 출력이 되게 된다.
"""