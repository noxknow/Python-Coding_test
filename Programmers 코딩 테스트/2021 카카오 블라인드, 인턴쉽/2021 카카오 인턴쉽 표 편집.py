def solution(n, k, cmd):
    answer = '' # linked_list는 해당 칸의 이전 값과 가르킬 값을 가지고 있습니다.
    linked_list = {i: [i-1, i+1] for i in range(1, n+1)} # 0~7보단 1~8까지가 표현하기 편해서 1~8로 지정
    cursor = k  + 1 # 1~8까지니 cursor에 + 1
    delete = [] # 삭제한 항목들을 담을 리스트
    res = ['O'] * n # 상태변화를 담은 리스트
    
    for i in cmd:
        # print('now cursor:', cursor)
        # print('now linked:', linked_list)
        if len(i)>1:
            state, x = i.split(' ') # cmd를 분해해서 상태와 숫자로 나눕니다.
            x = int(x)
            if state == 'D': # 'D'일 경우 숫자만큼 for구문을 돌려 cursor의 위치를 변화시킵니다.
                for _ in range(x):
                    cursor = linked_list[cursor][1]
                # print('D cursor:', cursor)
                # print('D linked :', linked_list)
            elif state == 'U': # 'U'일 경우 숫자만큼 for구문을 돌려 cursor의 위치를 변화시킵니다.
                for _ in range(x):
                    cursor = linked_list[cursor][0]
                # print('U cursor:', cursor)
                # print('U linked :', linked_list)
        
        else:
            if i=='C': # 'C'일 경우 현재 cursor의 이전값과 다음값을 가지고 시작합니다.
                prev, next = linked_list[cursor]
                delete.append((prev, cursor, next)) # delete에 넣습니다.
                res[cursor-1]='X' # curosor에 +1 을 해줬기에 다시 -1을하고 상태변화를 기록합니다.
                if next == n+1: # 다음 커서가 표를 벗어날경우 cursor를 이전값으로 설정합니다. (커서 상태만)
                    cursor = linked_list[cursor][0]
                else:
                    cursor = linked_list[cursor][1]
                if prev == 0: # 이 부분은 표에서 항목을 삭제한 후에 앞 뒤 항목의 값을 변경해줍니다. (앞, 뒤 값만)
                    linked_list[next][0] = prev
                elif next == n+1:
                    linked_list[prev][1] = next
                else:
                    linked_list[next][0] = prev
                    linked_list[prev][1] = next
                # print('C cursor:', cursor)
                # print('C linked :', linked_list)
            
            elif i=='Z': # 'Z'일 경우 delete에서 값을 빼냅니다.
                prev, now, next = delete.pop() # 가장 나중에 들어온걸 뺀다.
                res[now-1] = 'O' # 상테변화를 기억합니다.
                
                if prev==0: # 이 부분은 표에서 항목을 삭제한 후에 앞 뒤 항목의 값을 변경해줍니다.
                    linked_list[next][0] = now
                elif next == n+1:
                    linked_list[prev][1] = now
                else:
                    linked_list[prev][1] = now
                    linked_list[next][0] = now
                # print('Z cursor:', cursor)
                # print('Z linked :', linked_list)
    for x in res:
        answer += x
    return answer

if __name__ == '__main__': # 필요없는 부분
    print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))


"""
now cursor: 3
now linked: {1: [0, 2], 2: [1, 3], 3: [2, 4], 4: [3, 5], 5: [4, 6], 6: [5, 7], 7: [6, 8], 8: [7, 9]}
D cursor: 4
D linked : {1: [0, 2], 2: [1, 3], 3: [2, 4], 4: [3, 5], 5: [4, 6], 6: [5, 7], 7: [6, 8], 8: [7, 9]} 
D cursor: 5
cursor = linked_list[cursor][1] -> 의 의미 # 'D'일 경우 숫자만큼 for구문을 돌려 cursor의 위치를 변화시킵니다.
즉, linked_list[3][1] 은 3: [2, 4] limked list에서 4를 의미한다. 그래서 D cursor: 4

C cursor: 5
C linked : {1: [0, 2], 2: [1, 3], 3: [2, 4], 4: [3, 5], 5: [4, 6], 6: [5, 7], 7: [6, 8], 8: [7, 9]}
위에꺼가 아래꺼가 됨
C cursor: 6
C linked : {1: [0, 2], 2: [1, 3], 3: [2, 4], 4: [3, 6], 5: [4, 6], 6: [4, 7], 7: [6, 8], 8: [7, 9]}

4: [3, 5], 6: [5, 7]      ->        4: [3, 6], 6: [4, 7]
"""