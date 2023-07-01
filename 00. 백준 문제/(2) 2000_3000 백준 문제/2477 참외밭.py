s = [] # 방향, 거리 저장 리스트
x = [] # 가로 길이들 리스트
y = [] # 세로 길이들 리스트
lownum = [] # B의 가로 세로 길이
 
k = int(input())
 
for i in range(6):
    way,dist = map(int,input().split()) # 방향, 거리 입력
    s.append([way,dist])
    if s[i][0] == 3 or s[i][0] == 4: # 세로 저장
        x.append(s[i][1])
    if s[i][0] == 1 or s[i][0] == 2: # 가로 저장
        y.append(s[i][1])
 
# B의 길이 추출
for i in range(6):
    if s[i][0] == s[(i+2)%6][0]:
        lownum.append(s[(i+1)%6][1])
        
print( ((max(x)*max(y)) - (lownum[0]*lownum[1])) * k )
 


공감

'Problem Solving > CT-Python' 카테고리의 다른 글
[백준/DP] 16395: 파스칼의 삼각형 = [SWEA] 2005: 파스칼의 삼각형 - 파이썬  (0)	2022.04.25
[백준/브루트포스] 17614: 369 - 파이썬  (0)	2022.04.25
[SWEA] 1206: [S/W 문제해결 기본] 1일차 - View - 파이썬  (0)	2022.04.22
[백준/브루트포스] 2635: 수 이어가기 - 파이썬  (0)	2022.04.22
[백준/구현] 2669: 직사각형 네개의 합집합의 면적 구하기 - 파이썬  (0)	2022.04.22
'Problem Solving/CT-Python' 카테고리의 다른 글
[백준/DP] 16395: 파스칼의 삼각형 = [SWEA] 2005: 파스칼의 삼각형 - 파이썬
[백준/브루트포스] 17614: 369 - 파이썬
[SWEA] 1206: [S/W 문제해결 기본] 1일차 - View - 파이썬
[백준/브루트포스] 2635: 수 이어가기 - 파이썬

White Asher

이름 암호댓글쓰기
