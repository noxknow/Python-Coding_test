# def solution(d, budget):
#     answer = 0
    
#     d.sort()
#     cnt = 0
#     for i in range(len(d)):
#         if answer < budget:
#             answer += d[i]
#             cnt += 1
    
#     if answer > budget:
#         return cnt-1
#     else:
#         return cnt
    
def solution(d, budget):
    answer = 0
    
    d.sort()
    for i in range(len(d)):
        if d[i] <= budget:
            answer += 1
            budget -= d[i]
        else:
            break
    return answer
