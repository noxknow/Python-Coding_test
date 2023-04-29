# 효율성 따졌을 때 (O(1))
def solution(board, skill):
    answer = 0
    # 누적합 기록을 위한 배열 아래에 tmp[r2 + 1][c2 + 1] 이런식으로 board 배열보다 크게
    # 만들어지기 때문에 1칸씩 더 크게 tmp배열을 만들어 준다.
    tmp = [[0 for _ in range(len(board[0]) + 1)] for _ in range(len(board) + 1)]

    for type, r1, c1, r2, c2, degree in skill:
        # 누적합 기록, 부호에 주의할 것, 이렇게 참조한다면 O(1)
        tmp[r1][c1] += degree if type == 2 else -degree
        tmp[r1][c2 + 1] += -degree if type == 2 else degree
        tmp[r2 + 1][c1] += -degree if type == 2 else degree
        tmp[r2 + 1][c2 + 1] += degree if type == 2 else -degree
    
    # 행 기준 누적합
    for i in range(len(tmp) - 1): 
        for j in range(len(tmp[0]) - 1):
            tmp[i][j + 1] += tmp[i][j]
 
    # 열 기준 누적합
    for i in range(len(tmp) - 1): 
        for j in range(len(tmp[0]) - 1):
            tmp[i + 1][j] += tmp[i][j]
 
    # 기존 배열과 합함
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += tmp[i][j]
            # board에 값이 1이상인 경우 answer++
            if board[i][j] > 0: answer += 1
 
    return answer
    

# 효율성 안따지는 경우 (O(N*M))
def solution(board, skill):
    answer = 0
    for type, x1, y1, x2, y2, degree in skill:

        for i in range(x1,x2+1): # 여기서 2차원 배열요소를 일일이 참조해서 O(N*M)
            for j in range(y1,y2+1):
                board[i][j] += -degree if type == 1 else +degree # +=에서 -degree를 += 할지, +degree를 +=할지
    
    # if type == 1:
    #     for i in range(x1,x2+1):
    #         for j in range(y1,y2+1):
    #             board[i][j] -= degree
    # else:
    #     for i in range(x1,x2+1):
    #         for j in range(y1,y2+1):
    #             board[i][j] += degree

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] >= 1:
                answer += 1
    
    return answer

skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
print(solution(board, skill))

"""
[[ -N,  0,  0,  N,  0,  0],  (0,0) ~ (2,2) 까지 -N만큼 감소시키는 경우 배열은 이렇게 생성한다.
 [  0,  0,  0,  0,  0,  0],  -N이 행 으로 누적 합 하면 -N -N -N -N+N 0 0 이런식으로
 [  0,  0,  0,  0,  0,  0],  바뀌고 이걸 열기준으로 다시 누적합 해주면 된다.
 [  N,  0,  0, -N,  0,  0],
 [  0,  0,  0,  0,  0,  0],  위에서는 type == 2 일때 누적합을 적용시킨것 이지만,
 [  0,  0,  0,  0,  0,  0]]  여기서는 type == 1 일때 즉, N만큼 감소시키는 경우
                            이기 때문에 (0,0) = -N, (0,3) = N, (3,0) = N, (3,3) = -N
 [[ -N, -N, -N,  0,  0,  0], 이런 식으로 된거고 위의 경우는 반대인 경우로 해주면 된다.
 [  -N, -N, -N,  0,  0,  0],
 [  -N, -N, -N,  0,  0,  0],
 [  0,  0,  0,  0,  0,  0],
 [  0,  0,  0,  0,  0,  0],
 [  0,  0,  0,  0,  0,  0]]
"""