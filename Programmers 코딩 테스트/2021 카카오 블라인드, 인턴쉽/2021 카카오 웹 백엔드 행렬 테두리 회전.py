def solution(rows, columns, queries):
    answer = []
    
    board = [[0 for _ in range(columns+1)] for _ in range(rows+1)]
    for n in range(1,rows+1):
        for m in range(1,columns+1):
            board[n][m] = (n-1) * columns + m # 당연히 rows가 아니고 (n-1) * columns 생각해보면 됨

    for x1,y1,x2,y2 in queries:
        tmp = board[x1][y1]
        mini = tmp
    
        for k in range(x1,x2): # 좌측 열
            num = board[k+1][y1]
            board[k][y1] = num
            mini = min(mini, num)

        for k in range(y1,y2): # 아래 행
            num = board[x2][k+1]
            board[x2][k] = num
            mini = min(mini, num)

        for k in range(x2,x1,-1): # 우측 열
            num = board[k-1][y2]
            board[k][y2] = num
            mini = min(mini, num)

        for k in range(y2,y1,-1): # 위쪽 행
            num = board[x1][k-1]
            board[x1][k] = num
            mini = min(mini, num)
    
        board[x1][y1+1] = tmp
        answer.append(mini)
    
    return answer

rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(rows,columns,queries))

"""
좌측 열, 아래 행, 우측 열, 위쪽 행 순서
tmp = board[x1][y1] 이 값을 미리 저장해두지 않으면 좌측 열을 회전 시킬 때
사라지기 때문에 미리 저장해서 mini에 저장 해두고 좌측 열을 회전했으면 아래 행을
회전 시키는것이 편하기 때문에 저 순서로 회전을 시킨다. 

board[x1][y1+1] = tmp 요거는 미리 저장해둔 tmp값을 나중에 board[x1][y1+1]에 
넣어줘야 회전이 완벽하게 끝난 상태
"""