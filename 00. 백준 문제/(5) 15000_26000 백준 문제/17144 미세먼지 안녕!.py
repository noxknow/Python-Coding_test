import sys
sys.stdin=open("input.txt","r")
input = sys.stdin.readline

r, c, t = map(int, input().split())
board = []
for _ in range(r):
    board.append(list(map(int, input().split())))
new_board = [[0 for _ in range(c)] for _ in range(r)]
robot_top = 0
robot_bottom = 0

#상 우 하 좌
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def spread():  
    for x in range(r):
        for y in range(c):
            if board[x][y] > 0: # 미세먼지가 있는 경우
                tmp = 0
                for i in range(4):  # 4방면으로 퍼짐
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < r and 0 <= ny < c:  # board 에서 벗어나지 않는 범위일 경우만
                        if board[nx][ny] != -1:  # 공기청정기가 아닌 위치만 확산
                            new_board[nx][ny] += board[x][y]//5 # 확산값만 new_board에 넣어둔다.
                            tmp += board[x][y]//5
                board[x][y] -= tmp
    for x in range(r):
        for y in range(c):
            board[x][y] += new_board[x][y] # 확산값을 더해주면 완성

def rotation():
    def top_rotate(): # 위쪽 회전
        d = 1 # 오른쪽 방향으로 시작
        before = 0
        x, y = robot_top, 1 # 공기청정기 머리부분의 바로 오른쪽 칸부터 시작
        while True:
            nx = x + dx[d]
            ny = y + dy[d]
            if nx == r or ny == c or nx == -1 or ny == -1: # 현재 좌표가 꼭짓점인 경우
                d = (d-1)%4 # 꼭짓점을 만나면 우 -> 상 -> 좌 -> 하 으로 바뀐다. (d=-1인 경우 나머지 3)
                continue
            if x == robot_top and y == 0: # 한 바퀴 회전 완료해서 공기청정기 좌표로 다시 돌아온 경우
                break
            board[x][y], before  = before, board[x][y] 
            # board[2][1]은 2, before = 0이니, board[2][1] = 0, before = 2가 된다. 
            # 다음에 board[2][2] = before = 2가 됨. before = 원래 board[2][2]이 되고,  
            x, y = nx, ny # 좌표가 계속 이동


    def bottom_rotate():  
        d = 1 
        before = 0
        x, y = robot_bottom, 1 
        while True:
            nx = x + dx[d]
            ny = y + dy[d]
            if nx == r or ny == c or nx == -1 or ny == -1: 
                d = (d+1)%4
                continue
            if x == robot_bottom and y == 0: 
                break
            board[x][y], before  = before, board[x][y]
            x, y = nx, ny
            
    top_rotate()
    bottom_rotate()


for i in range(r): # 공기청정기의 위치를 찾기 위함
    if board[i][0] == -1:
        robot_top = i
        robot_bottom = i+1
        break

for _ in range(t): # t만큼 수행
    spread() 
    rotation() 
    
answer = 2  #공기청정기 2칸 -1인 것 상쇄하기 위함
for i in range(r):
    answer += sum(board[i])
print(answer)
