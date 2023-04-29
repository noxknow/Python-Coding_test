def solution(gems):
    answer = []
    shortest = len(gems)+1 
    
    start_p = 0
    end_p = 0
    
    size = len(set(gems)) # 보석의 총 종류 수
    contained = {} # 현재 구간에 포함된 보석들(종류: 갯수)
    
    while end_p < len(gems): # 구간의 끝 점이 gems의 길이보다 작을 동안
        if gems[end_p] not in contained: # 현재 끝 점의 보석이 contained에 없다면
            contained[gems[end_p]] = 1 # dictionary에 추가  
        else:
            contained[gems[end_p]] += 1 # 이미 있으면 dictionary에 +1
        end_p += 1  # 끝 점을 나중에 증가
    
        if len(contained) == size:
            while start_p < end_p:
                if contained[gems[start_p]] > 1: # start_p에 해당하는 보석이 구간 내에 하나 이상 있다면
                    contained[gems[start_p]] -= 1
                    start_p += 1
                
                elif shortest > end_p - start_p:
                    shortest = end_p - start_p # 최단거리 갱신
                    answer = [start_p+1, end_p]
                    break
                
                else:
                    break
    
    return answer

"""
투포인터

shortest에서 len(gems)+1 1을 더해준 이유는 만약 길이가 3일 때 end와 start는 인덱스 상으로 2까지
가는데 end의 경우 마지막에 1을 더 더해주기 때문에 3까지 갈 수 있다. 이때 end - start는 3이므로
shortest와 같게 되므로 +1을 해줌으로써 shortest > end_p - start_p를 성립시켜 준다.

shortest > end_p - start_p 에서 shortest >= end_p - start_p 이렇게 된다면 1 3과 2 4가 
end - start가 같아서 2 4가 정답이 되기 때문에 shortest > end_p - start_p이렇게 되어야
1 3이 정답이 된다.

shortest = end_p - start_p # 최단거리 갱신 
요거 없으면 [3,7] 이 답인데 나중에 [3,8]도 가능은 하기 때문에 젤 나중에 나오는 [3,8]이 답이 되버린다.

보석쇼핑 answer = [] 일 때 
answer.append([a,b]) 이렇게 넣으면 answer = [[a,b], []] 로 이중 리스트가 되니깐 answer = [a, b] 해주면
리스트에 값이 들어간 꼴이 된다.

if if 가 아닌 if elif 해야 맨 위에 if 에서 걸리게 되면 elif를 안할수 있다.
"""