from itertools import permutations

def solution(k, dungeons):
    answer = []
    permu = list(permutations(dungeons, len(dungeons)))
    for per in permu:
        cnt = 0
        num = k
        for tmp in per:
            if num >= tmp[0]:
                num -= tmp[1]
                if num < 0:
                    break
                cnt += 1
        answer.append(cnt)
                  
    return max(answer)
