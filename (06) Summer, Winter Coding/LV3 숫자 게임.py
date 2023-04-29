# from itertools import permutations

# def solution(A, B):
#     answer = []
    
#     permu = list(permutations(B,4))   시간 초과
#     for per in permu:
#         res = 0
#         for i in range(len(per)):
#             if A[i] < B[i]:
#                 res += 1
#         answer.append(res)
    
#     return max(answer)

def solution(A, B):
    answer = 0
    
    A.sort()
    B.sort()
    
    ai, bi = 0, 0
    while ai != len(A) and bi != len(B):
        if B[bi] > A[ai]:
            answer += 1
            ai += 1
            bi += 1
        else:
            bi += 1
        
    return answer
