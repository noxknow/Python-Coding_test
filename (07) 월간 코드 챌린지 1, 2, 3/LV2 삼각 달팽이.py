def solution(n):
    answer = [[0 for j in range(1, i+1)] for i in range(1, n+1)]
    
    x, y = -1, 0 # 첫번째 턴에서 x+=1해주면 answer[0][0] 으로 좌표가 나오게 된다.
    num = 1
    
    for i in range(n):
        for j in range(i,n):
            if i%3 == 0: # 아래로 내려갈 때 행이 늘어나니 x좌표값이 늘어난다
                x += 1
            elif i%3 == 1: # 우측으로 가면 열이 늘어나니 y좌표값이 늘어난다.
                y += 1
            else:
                x -= 1
                y -= 1
            answer[x][y] = num
            num += 1
    
    return "[]".join(answer)
