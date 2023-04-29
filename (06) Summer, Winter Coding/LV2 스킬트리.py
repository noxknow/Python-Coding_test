def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        s = ""
        for t in tree:
            if t in skill:
                s += t
                
        if skill[:len(s)] == s:
            answer += 1
    
    return answer
