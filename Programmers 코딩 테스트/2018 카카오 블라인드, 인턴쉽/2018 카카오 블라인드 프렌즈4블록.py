def solution(m, n, board):
    for i in range(m):
        board[i] = list(board[i]) # 여기서 문자열 형태인 board를 list로 만들어준다.

    stack = set() # 리스트 형식이 아닌 집합 형식이여야 중복 값이 사라진다.
    cnt = 0
    
    while True:
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == []: # 이거 없으면 시간 엄청 오래걸린다. 아닌경우 continue로 빠르게 다음루프로 넘겨야 함.
                    continue

                if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                    stack.add((i,j)) # 집합 형식의 경우 add를 사용하고 (()) 괄호 두개 사용.
                    stack.add((i,j+1))
                    stack.add((i+1,j))
                    stack.add((i+1,j+1))

        if len(stack) > 0:
            cnt += len(stack)
            for i,j in stack:
                board[i][j] = [] # 좌표 삭제 
            stack = set() # 여기서 한번 stack에 추가한거 초기화 stack = [] 리스트 초기화 하는 느낌
        else: 
            return cnt

        while True:
            moved = 0
            for i in range(m-1):
                for j in range(n):
                    if board[i][j] and board[i+1][j] == []:
                        board[i+1][j] = board[i][j]
                        board[i][j] = []
                        moved += 1
                        
            if moved == 0:
                break


n = 6
m = 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
print(solution(m, n, board))