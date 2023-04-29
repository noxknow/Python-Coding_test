# N이 5,000일 때
# 5000 -> 2500 -> 1250 -> 625(ans + 1) -> 312 -> 156 -> 78 -> 39(ans + 1) -> 19(ans + 1) -> 9(ans + 1) -> 4 -> 2 -> 1(ans + 1) 따라서 건전지 사용량은 5가 된다. 2로 안 나눠떨어질 때

def solution(n):
    answer = 1
    
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            answer += 1
            n -= 1
    
    return answer
