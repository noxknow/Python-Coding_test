from collections import Counter

def solution(str1, str2):
    answer = 0
    str1_low = str1.lower()
    str2_low = str2.lower()
    
    str1_lst = []
    str2_lst = []
    
    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i+1].isalpha(): # isalpha() 문자열 인지 확인한다.
            str1_lst.append(str1_low[i:i + 2])

    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            str2_lst.append(str2_low[i:i + 2])
            
    Counter1 = Counter(str1_lst) # 다중 집합을 허용 하기 위해서 ex) ({"aa" : 2})
    Counter2 = Counter(str2_lst) # ex) ({"aa" : 3}) -> ['aa', 'aa', 'aa']
    
    inter = list((Counter1 & Counter2).elements()) # 아래 설명 ['aa', 'aa'] 
    union = list((Counter1 | Counter2).elements()) # ex) ['aa', 'aa', 'aa']
    # print(inter, union)
    
    if len(union) == 0 and len(inter) == 0:
        answer = 65536
        return answer
    else:
        answer = int(len(inter) / len(union) * 65536) # int(x)는 x를 버림 한다는 의미
        return answer
    
str1 = "aa1+aa2"
str2 = "AAAA12"
print(solution(str1, str2))

"""
Counter 메서드는 각각의 리스트는 해당 원소값을 key값으로 하고, 원소의 갯수를 value값으로 하는 dictionary 형태의 구조를 반환한다.
예를 들어 str1 = FRANCE, str2 = french 라면, 이 로직을 거쳤을 경우 Counter1과 Counter2는 각각 다음의 값을 출력한다.

print(Counter1, Couner2)
>>> Counter1({'fr': 1, 'ra': 1, 'an': 1, 'nc': 1, 'ce': 1}) Counter2({'fr': 1, 're': 1, 'en': 1, 'nc': 1, 'ch': 1})

예를 들어 counter 함수를 통해 ({"aa" : 2}) 라는 결과를 얻었으면
Counter1.elements() 는 ['aa', 'aa']로 표현된다.

import math

    if len(inter) == 0 and len(union) == 0:
        answer = 65536
    else:
        answer = (len(inter) / len(union)) * 65536
    
return math.floor(answer)

이걸로도 버림이 가능
"""