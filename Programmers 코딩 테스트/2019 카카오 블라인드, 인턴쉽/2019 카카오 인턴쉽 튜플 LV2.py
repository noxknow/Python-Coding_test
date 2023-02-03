def solution(s):
    s = s[2:-2]
    s = s.split("},{")
    s.sort(key = len)
    
    answer = []
    for i in s:
        tmp = i.split(",")
        for j in tmp:
            if int(j) not in answer:
                answer.append(int(j))      
    return answer

# s = input() 
# print(solution(s))

"""
* a[0:3]이 수식을 만족하는 것은 a[0], a[1], a[2]이다. 따라서 a[0:3]은 'Lif'이고 
  a[0:4]는 'Life'가 되는 것이다. 이 부분이 문자열 연산에서 가장 혼동하기 쉬운 부분이니 
  장 마지막의 연습 문제를 많이 풀어 보면서 몸에 익히기 바란다.

  위 소스 코드에서 a[19:-7]이 뜻하는 것은 a[19]에서부터 a[-8]까지를 말한다. 
  이 역시 a[-7]은 포함하지 않는다.
"""