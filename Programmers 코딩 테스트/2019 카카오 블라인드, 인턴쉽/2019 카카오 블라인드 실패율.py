# 시간복잡도 O(n)
def solution(N, stages):
    people = len(stages)
    fail = {}
    for i in range(1, N+1):
        if people != 0:
            fail[i] = stages.count(i) / people
            people -= stages.count(i)
        else:
            fail[i] = 0
    
    fail = sorted(fail.items(), key=lambda x: (-x[1], x[0]))
    fail = dict(fail) 
    answer = list(fail.keys())
        
    return answer # return sorted(fail, key=lambda i: -fail[i]) 위에 3줄 압축가능

# 시간복잡도 O(n^2) 이라 런타임 에러....
def solution(N, stages):
    dic = {}
    for stage in stages:
        for i in range(1, stage+1):
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
                
    fail = {}
    for i in range(1, N+1):
        if dic.get(i) == "None":
            fail[i] = 0
        else:
            fail[i] = stages.count(i) / dic[i]
    
    fail = sorted(fail.items(), key=lambda x: (-x[1], x[0])) # 딕셔너리는 dic.sort() 안되고, dic = sorted(dic, ~) 그리고 딕셔너리 정렬하려면 dic.items() 해줘야 한다.
    fail = dict(fail) # 리스트를 다시 딕셔너리로 
    answer = list(fail.keys()) # 딕셔너리의 키 값을 리스트화 시킨다.
        
    return answer

# answer = []
# for i in range(len(fail)):
#     answer.append(fail[i][0])

stages = [2, 1, 2, 6, 2, 4, 3, 3]
N = 5
print(solution(N, stages))

"""
d = {1 : 1, 2 : 1}
원래 키값이 없을 때 d[3]으로 불러오려고 하면 에러가 나오지만, d.get(3)를 한다면 None가 나오게 된다.
그런데 int와 None은 더할 수 없습니다. 그러면 어떻게 해야 할까요? 사실, 서점에 없는 책은 구입할 필요가 
없으니, 키가 없을 때 리턴할 default value를 설정하면 됩니다. 이는 2번째 인자에서 설정할 수 있습니다.
문서에도 default 값에 대한 것이 언급되어 있습니다.

book_store = {"a" : 1000, "k" : 2000, "h" : 1000}  --> 아까 코드와 달라진 점은 get 부분입니다. 2번째 
buy_list = ["a", "m", "ra", "k"]                       인자에 0 이 들어갔는데요. 이는 키가 없을 때 0을 리턴하라는 의미입니다.
print(sum([book_store.get(k, 0) for k in buy_list]))

[book_store.get(k, 0) for k in buy_list] 
--> 의미는 k에 buy_list 값을 for stage in stages: 느낌으로 집어 넣고 그 값을 book_store.get(k, 0)의
k값에 넣어서 리스트를 만들어 주는 것!

sorted(fail, key=lambda i: fail[i], reverse=True)의 의미는 i는 fail이라는 딕셔너리의 키 값을 의미하므로
fail[i]는 (fail[1] : 0.5라면 i가 1일때 0.5값이 나옴) value 값이 나오고 그것을 reverse 
= True 하면 -x[1]이란 의미 즉, value의 내림차순을 의미하고 딕셔너리 정렬에서 fail.items()
할 때만 출력에 key, value가 둘 다 나오니 fail만 써서 key값만 오름차순으로 정렬한것을 의미한다.
--> 한마디로 value 값을 내림차순하고 key 값만 오름차순으로 출력한다.
"""

