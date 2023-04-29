def solution(new_id):
    answer = ''

    for id in new_id.lower():
        if id.isalnum() or id in ["-", "_", "."]: # 혹은 id in "-_."
            answer += id

    while ".." in answer:
        answer = answer.replace("..", ".")
        
    if answer[0] == "." and len(answer) > 1: 
        answer = answer[1:] # len(answer) 아니면 "=.=" 이 경우 다음 if에서 오류 난다.
    if answer[-1] == ".":
        answer = answer[:-1]
    
    if answer == "": # 혹은 if not answer:
        answer += "a"
          
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == ".":
            answer = answer[:-1]

    while len(answer) <= 2:
        answer += answer[-1]
            
    return answer

new_id = "...!@BaT#*..y.abcdefghijklm"
print(solution(new_id))