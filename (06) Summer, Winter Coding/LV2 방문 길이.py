def solution(dirs):
    answer = 0
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    d = {"U" : 0, "D" : 1, "L" : 2, "R" : 3}
    
    visited = set()
    x, y = 0, 0
    for dir in dirs:
        nx = x + dx[d[dir]]
        ny = y + dy[d[dir]]
        
        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            continue
        
        if (x,y,nx,ny) not in visited:
            visited.add((x,y,nx,ny))
            visited.add((nx,ny,x,y))
            answer += 1
        
        x,y = nx,ny
        
    return answer
