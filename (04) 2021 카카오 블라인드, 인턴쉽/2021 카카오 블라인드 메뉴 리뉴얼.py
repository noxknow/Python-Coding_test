from itertools import combinations
from collections import Counter

# 다른사람이 푼 것
def solution(orders, course):
    answer = []
    
    for c in course:
        temp = []
        
        for order in orders:
            combi = combinations(sorted(order), c) # sorted는 자동적으로 오름차순 정렬 해주니 (w,x) == (x,w)가 되도록 해준다.
            temp += combi
            
        counter = Counter(temp)

        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]

    return sorted(answer)

# 내가 한 것
def check(array):
    counter = Counter(array)
    res = []
    if len(counter) != 0 and max(counter.values()) != 1:
        for i in counter:
            if counter[i] == max(counter.values()):
                res += ["".join(i)]

    return res
        
def solution(orders, course):
    answer = []
    
    for num in course:
        arr = []
        for order in orders:
            combi = list(combinations(sorted(order), num))
            arr += combi
        tmp = check(arr)
        answer += tmp
    
    return sorted(answer)

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
print(solution(orders, course))

"""
a = [1,2,3]
list(permutations(a, 2)) : [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
list(combinations(a, 2)) : [(1, 2), (1, 3), (2, 3)]

list(permutations(a, 3)) : [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
list(combinations(a, 3)) : [(1, 2, 3)]

itertools.permutations('ABCD', 2)
# 결과: AB AC AD BA BC BD CA CB CD DA DB DC

itertools.combinations('ABCD', 2)
# 결과: AB AC AD BC BD CD

itertools.combinations_with_replacement('ABCD', 2)
# 결과: AA AB AC AD BB BC BD CC CD DD

위에서 ["XYZ", "XWY", "WXA"] 인 경우 "wxa" 를 sorted 해주면 "awx"가 되고, "xwy"
도 "wxy"가 되므로 permutations, combinations에서 제거하는 (1, 2) (2, 1)과 다르게
('W', 'X'): 1, ('X', 'W'): 1   -->  ('W', 'X'): 2 이렇게 된다.
combinations에서 순서 제거하고 sorted로 또 한번 이상한 부분 제거

arr = [] 이런식으로 리스트를 만들 때 추가해주려면 arr.append()만 생각했는데
arr += 이런식으로 추가해준다면 for문을 도는 동안 2중 리스트가 append되는것이 아니라
기본적인 리스트 형태로 들어가게 된다. 

str 아닐 때 join --> "".join(map(str, n))

print(["".join(("x","y","c"))]) --> ["xyc"]
print("".join(("x","y","c"))) --> xyc
print("".join("x","y","c")) --> 이러면 join안에 3개의 요소가 들어간걸로 판단하기
때문에 "x","y","c" 이게 아니라 ("x","y","c") 하나로 묶어서 들어가주면 join가능

dic = {(5, 6) : 1, (3,4) : 2}
for i in dic:
    print(dic[i])       이러면  1 2
    print(i)            이러면 (5,6) (3,4)

counter[i]의 의미는 counter가 dictionary형식이니 ('X', 'Y'): 2 식 이면 
counter[("x", "y")] = 2 인 의미이다.

for i in counter:
    if counter[i] == max(counter.values()):
        res += ["".join(i)]

== answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]
"""
