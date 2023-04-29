def solution(sticker):
    if len(sticker) <= 3:
        return max(sticker)
    
    answer = 0
    dp1 = [0 for _ in range(len(sticker))] # 첫 번째 선택
    dp2 = [0 for _ in range(len(sticker))] # 첫 번째 선택 x
    
    dp1[0], dp1[1] = sticker[0], sticker[0] # 첫 번째를 사용하는경우 dp1[1]도 sticker[0] 이다.(sticker[1] 고를 수 없음)
    dp2[0], dp2[1] = 0, sticker[1]
    
    for i in range(2, len(sticker)):
        if i == len(sticker)-1: # dp1의 경우 첫번째를 골라서 마지막을 고를 수 없기에 여기에 쓰지 않는다.
            dp2[i] = max(dp2[i-1], sticker[i]+dp2[i-2])
        else:
            dp1[i] = max(dp1[i-1], sticker[i]+dp1[i-2])
            dp2[i] = max(dp2[i-1], sticker[i]+dp2[i-2])
    
    answer = max(dp1[len(dp1)-2], dp2[len(dp2)-1]) # dp1은 마지막을 고르지 않았기 때문에 -2 해줘야 하고 dp2는 마지막을 골랐기 때문에 -1만 한다면 마지막 인덱스이다.

    return answer
