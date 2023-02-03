# 딕셔너리 이용 (10816 숫자 카드 2 (이분탐색))
import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

dic = Counter(n_list) # 이렇게도 표현가능하고, 아래처럼도 가능하다.
# dic = {}
# for i in n_list:
#     if i in dic:
#         dic[i] += 1
#     else:
#         dic[i] = 1

for i in m_list:
    if i in dic:
        print(dic[i], end = " ")
    else:
        print(0, end = " ")

# 2018 카카오 블라인드 다트 게임
def solution(dartResult):
    stack = []
    dartResult = dartResult.replace("10" , "A")
    bonus = {"S" : 1, "D" : 2, "T" : 3}
    
    for i in dartResult:
        if i.isdigit() or i == "A":
            stack.append(10 if i == "A" else int(i))
        elif i.isalpha():
            num = stack.pop()
            stack.append(num ** bonus[i]) # 혹은 한번에 stack[-1] **= bonus[i]
        elif i == "#":
            stack[-1] *= -1
        elif i == "*":
            num = stack.pop()
            if len(stack):
                stack[-1] *= 2
            stack.append(num*2)
            
    return sum(stack) # print(sum(stack))

dartResult = "1D#2S*3S"
solution(dartResult)

# 2018 카카오 블라인드 압축
def solution(msg):
    answer = []
    dic = {chr(64+i) : i for i in range(1,27)} # chr(65) = "A", chr(66) = "B"
    cnt = 27
    i = 0
    search = ""

    while i < len(msg):
        search += msg[i]
        # print(search) 해보면 마지막에 O가 남는걸 볼 수 있다.

        if search in dic:
            i += 1
    
        else:
            dic[search] = cnt
            cnt += 1

            s = search[:-1]
            answer.append(dic[s])
            search = ""

    answer.append(dic[search]) #  # search에 마지막 글자 남아있으니 마지막 글자의 색인번호 answer에 append
    
    return answer # print(answer)

msg = "KAKAO"
solution(msg)
