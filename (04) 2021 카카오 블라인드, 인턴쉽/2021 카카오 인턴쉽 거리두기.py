from collections import deque

# places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

def solution(places):
    answer = []
    for i in places: 
        answer.append(bfs(i))
    return answer # print(answer)

def bfs(p):
    start = []
    for i in range(5):
        for j in range(5):
            if p[i][j] == 'P':
                start.append([i, j]) # 'P'가 있는 시작점들 모으기

    for s in start: # 시작점리스트에서 1개씩 시작
        q = deque([(s)])
        visited = [[0 for _ in range(5)] for _ in range(5)]
        distance = [[0 for _ in range(5)] for _ in range(5)] # 시작점 'P'와 'O'를 체크하여 거리 계산
        visited[s[0]][s[1]] = 1 
        
        while q:
            x, y = q.popleft() # q를 시작점이라고 생각하면 편합니다. 
            
            for i in range(4): 
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<5 and 0<=ny<5 and visited[nx][ny] == 0: 
                   
                   if p[nx][ny] == 'O': # 시작점을 기준으로 상, 하, 좌, 우 중 'O'를 발견시
                        q.append((nx, ny)) # 'O'의 자리를 다시 시작점으로 설정
                        visited[nx][ny] = 1 # 'O'의 자리를 확인했으니 1로 체크
                        distance[nx][ny] = distance[x][y] + 1 # 시작점에서부터 거리 + 1
                        
                   if p[nx][ny] == 'P' and distance[x][y] <= 1: # 시작점을 기준으로 상, 하, 좌, 우 중 'P'를 발견했고 이때 시작점부터의 거리가 1보다 작거나 같을 경우, 즉, 따지자면 p[nx][ny] == 'P' 요 자리는 distance[nx][ny] 이게 2가 되는 자리이기에 그 전 자리인 distance[x][y] <= 1는 1이하가 맞다.
                        return 0 # 0을 리턴하고 반복문 종료, 거리가 2인 경우는 거리두기를 한 것이기에 무시
    return 1

# solution(places)

"""
1번 시나리오 상황
전체     P만       P 1개    O 거리
POOOP P===P  =OOO= 00000
OXXOX =====  O==O= 20000
OPXPX  =P=P=  OP===  1P000
OOXOX ===== OO=O= 21000
POXXP  P===P  =O=== 02000

2번 시나리오 상황
전체     P만        P 1개    O 거리
POOPX P==P=   POO=O P1200
OXPXP  ==P=P  O====  10000
PXXXO  P====  S===O  S0000
OXXXO =====  O===O 00000
OOOPP ===PP  OOO== 00000

이런식으로 3번째와 4번쨰 예시를 보시면 하나의 P를 기준으로 주변의 O를 찾으면서 거리를 계산했습니다.
1번같은경우는 P주변에 O의 거리를 계산했을경우 또다른 P가 없었기에 거리만 계산되었고
2번같은경우는 P주변에 O의 거리를 계산했는데 S라는 또다른 P가 있었고 P와 S간의 거리가 1(시작점)밖에 안되기에
0을 리턴하게 됩니다.
"""