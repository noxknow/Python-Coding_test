# 성실한 개미
ant_house = [
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 1, 1, 1, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
         [1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
         [1, 0, 0, 0, 0, 1, 2, 1, 0, 1],
         [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
"""
ant_house = []
for i in range(10):
  matrix = list(map(int, input().split()))
  ant_house.append(matrix) 도 가능하다는 것 같음 하나씩 채우는 느낌
"""
x, y = 1, 1
while ant_house[x][y] != 2:
  if ant_house[x][y] == 0:
    ant_house[x][y] = 9
    y += 1
  else:
    x += 1
    y -= 1
ant_house[x][y] = 9

for house in ant_house :
  print( *house )