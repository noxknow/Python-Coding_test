def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])    # 0이 아닌 경우만 뽑아 stacklist(바구니) 에 넣음
                board[j][i-1] = 0    # 뽑힌 숫자(인형)은 0으로 변경

                # stacklist(바구니)에 인형이 2개 이상 있을때마다 확인
                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:    # 맨 마지막 두 개의 숫자가 같으면
                        stacklist.pop(-1)    #
                        stacklist.pop(-1)    # 그 두개를 pop 그냥 pop()해도 상관 없다.
                        answer += 2     
                
                break # 인형을 찾은 뒤 굳이 남은 아래칸들을 뒤질 필요가 없으니 for문에서 나가기 위해 break를 겁니다.

    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))
"""
moves는 열을 나타내는 거라 for j in range(len(board)) 이게 먼저 오고 for i in moves 오는게
맞지만 이 문제에서는 moves에 나오는 열의 값에 따라 그 열에 대해서 행들을 조사해야 하므로
moves를 i로 해서 for문을 먼저 등장시키는게 맞다.

break는 반복문을 탈출시켜주기 때문에 이 점을 생각하고 써주면 된다.
"""
