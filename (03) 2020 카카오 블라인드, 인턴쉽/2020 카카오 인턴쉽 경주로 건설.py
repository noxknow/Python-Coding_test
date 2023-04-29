from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# n = int(input())
# board = []
# for _ in range(n):
#     board.append(list(map(int, input().strip())))

def bfs(board, z):
    n = len(board)
    price = [[1e9 for _ in range(n)] for _ in range(n)] # 가격값을 1e9 즉 max(무한)으로 채워둔다.
    price[0][0] = 0

    q = deque([(0,0,0,z)])

    while q:
        x, y, c, z = q.popleft()

        # if x == n - 1 and y == n - 1: 없어도 됨
        #     continue 

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = i

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                if nz == z:
                    nc = c + 100 
                else:
                    nc = c + 600

                if nc < price[nx][ny]:
                    price[nx][ny] = nc
                    q.append((nx, ny, nc, nz))

    return price[-1][-1]


def solution(board):
    answer = min(bfs(board, 1), bfs(board, 3)) # z의 경우 오른쪽과 아래로 가는 경우 두개만 비교하면 되기 때문에
    return answer

# print(solution(board))

"""
break가 아니라 continue인 이유 z를 오른쪽과 아래 두가지 경우로 구하려했는데, break를 쓰는경우 
오른쪽에서 x == n-1에 도달해 버리면 아래쪽으로 가는 경우의 수는 하지않고, 끝내 버리기 때문에
continue를 통해 오른쪽이 x == n-1에 도달해도 아래쪽의 경우의 수도 같이 하여 min을 구해주는 역할
continue는 이번 루프는 끝내고 다음 루프를 계속하겠다는 의미

for i in range(10):                 -->  1
    if i % 2 == 0:                       3
        continue                         5
        print(i)                         7
    print(i)                             9
print("Done")                            Done

위의 결과를 보면 i가 2의 배수인 경우에는 continue가 실행됩니다.
continue가 실행되면 해당 부분을 그냥 넘어가게됩니다. 해당 순번의 loop를 넘어가 다음번 loop로 들어가게됩니다. 
따라서 if문 안에 있는 print문과 if문 밖의 print문 둘 다 실행되지 않고 다음 loop로 넘어갑니다.

nc < price[nx][ny] 여기에서 price[nx][ny]는 max로 계속 유지되고 price[nx][ny] = nc이게 nc로
바뀌게 된다음, q.append((nx, ny, nc, nz))를 통해 x, y, c, z = q.popleft() 여기서 c가 nc가 된다.
ex) 처음 c = 0 그담 직진이라 c + 100 으로 nc = 100이면 price[1][1] = 100 그럼 c = 100 그 담 또
직진 nc = 200, nc < price[nx][ny] -> 200 < max 이므로 price[2][2] = 200 이런식
"""