def solution(record):
    answer = []

    dic = {}   
    for name in record:
        tmp = name.split() # 공백 기준으로 짜르기
        if tmp[0] != "Leave": # tmp[0] == "Enter" or tmp[0] == "Change" 도 가능
            dic[tmp[1]] = tmp[2]

    for name in record:
        tmp = name.split()
        if tmp[0] == "Enter":
            answer.append(dic[tmp[1]] + "님이 들어왔습니다.") # answer.append('%s님이 들어왔습니다.' %dic[tmp[1]])
        elif tmp[0] == "Leave":
            answer.append(dic[tmp[1]] + "님이 나갔습니다.")
    
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))