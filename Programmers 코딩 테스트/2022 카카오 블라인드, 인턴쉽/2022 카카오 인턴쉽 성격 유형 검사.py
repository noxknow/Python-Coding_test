from collections import defaultdict
score = [0,3,2,1,0,1,2,3]

def solution(survey, choices):
    answer = ''
    num_list = defaultdict(int)
    
    for i in range(len(survey)):
        num_list[survey[i][choices[i] // 4]] += score[choices[i]]
    
    answer += "R" if num_list["R"] >= num_list["T"] else "T"
    answer += "C" if num_list["C"] >= num_list["F"] else "F"
    answer += "J" if num_list["J"] >= num_list["M"] else "M"
    answer += "A" if num_list["A"] >= num_list["N"] else "N"
    
    return answer

survey = ["TR", "RT", "TR"] 
choices = [7, 1, 3]
print(solution(survey, choices))

# zip으로 survey랑 choices를 묶으려 했으나 사전형식에서는 TR처럼 똑같은게 두번 나온다면
# 마지막에 나온 값 만 적용되기 때문에 위처럼 해야한다.