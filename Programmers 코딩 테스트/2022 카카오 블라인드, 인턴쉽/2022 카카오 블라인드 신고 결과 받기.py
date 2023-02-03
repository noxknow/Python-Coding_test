from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    dic = defaultdict(list) # dic[re[0]] = re[1] 이런식으로 하면 muzi가 두번 신고했는데 마지막 신고만 들어가게 된다.
    cnt = defaultdict(int) # int형으로 해야 신고 안당한 경우도 apeach : 0 이런식으로 나와 에러가 안나온다.

    for r in report:
        re = r.split()
        dic[re[0]].append(re[1])
        cnt[re[1]] += 1
    
    for i in id_list:
        res = 0
        for u in dic[i]: # muzi가 신고한 두개에 대해서 메일을 받야야 하므로
            if cnt[u] >= k:
                res += 1
        answer.append(res)
        
    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(solution(id_list, report, k))

"""
defaultdict가 없었다면 

dic = {}               
if re[0] not in dic:            --> 이런식인데 이렇게 하면 아래처럼 나오게 된다.
    dic[re[0]] += re[1]    {'muzi': 'frodoneo', 'apeach': 'frodomuzi', 'frodo': 'neo'}
else:
    dic[re[0]] = re[1]
"""