import math

def solution(n, stations, w):
    answer = 0
    range = w*2 + 1
    
    now = 1
    for station in stations:
        length = station - w - now # 첫번째 아파트부터 station에서 w만큼 간거에 1칸을 더 빼줘야 
        if length > 0: # 전파가 닿지않는 범위가 된다.   
            answer += math.ceil(length/range)
        now = station + w + 1 # now를 앞에 안 닿는 범위는 해결했으니 뒷부분도 해주기 위해 바꿔준다.
        
    if n >= now:
        answer += math.ceil((n-now+1)/range)

    return answer
