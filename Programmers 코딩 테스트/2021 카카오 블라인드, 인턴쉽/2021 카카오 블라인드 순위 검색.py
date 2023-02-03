from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

# 효율성에서 틀리는 문제
def solution(info, query):
    answer = []
    
    for querys in query:
        res = 0
        tmp = querys.replace("and", "").split()
        for infos in info:
            cnt = 0
            infos = infos.split(" ")
            for i in range(4):
                if infos[i] == tmp[i] or tmp[i] == "-":
                    cnt += 1
            if cnt >= 4 and int(infos[4]) >= int(tmp[4]):
                res += 1
        answer.append(res)
            
    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))

"""
파이썬 bisect 라이브러리의 bisect_left는 lower bound
Lower Bound는 '원하는 값 이상이 처음 나오는 위치를 찾는 과정' 이며, 
Upper Bound는 '원하는 값을 초과한 값이 처음 나오는 위치를 찾는 과정'입니다.

from bisect import bisect_right, bisect_left

lst= [1, 4, 6, 10]
print(bisect_left(lst, 6)) # result = 2,     print(bisect_left(lst, 9)) # result = 3
print(bisect_right(lst , 6)) # result = 3,   print(bisect_left(lst, 9)) # result = 3

1. 해당 값이 리스트에 있을 때            2. 해당 값이 리스트에 없을 때
bisect_left - 해당 index 반환           리스트 오름차순에 들어갈 index 반환
bisect_right - 해당 index+1 반환        리스트 오름차순에 들어갈 index 반환

tmp = querys.split(" ")         -->         tmp = querys.replace("and", "").split()
    for i in range(3):
        tmp.remove("and")

split은 공백기준이니 만약 replace를 "and"를 한다 하면 공백이 두칸이 나오게 되는데 이때
.split(" ") 한다면 공백 한칸만을 기준으로 split 하기 때문에
['java', '', 'backend', '', 'junior', '', 'pizza', '100'] 이런식으로 나온다.
하지만 split() 해준다면 두칸 공백도 모두 없애서 계산해준다.
"""