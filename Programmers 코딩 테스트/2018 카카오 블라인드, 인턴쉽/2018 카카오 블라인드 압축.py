# 방법 1
def solution(msg):
    answer = []
    dic = {chr(64+i) : i for i in range(1,27)} # chr(65) = "A", chr(66) = "B"
    cnt = 27
    i = 0
    search = ""

    while i < len(msg):
        search += msg[i]
        # print(search) #해보면 마지막에 O가 남는걸 볼 수 있다.

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

# 방법 2

def solution(msg):
    answer = []

    dic = {}
    for i in range(26):
        dic[chr(65+i)] = i+1

    w, c = 0, 0
    while True:
        c += 1
        if c == len(msg):
            answer.append(dic[msg[w:c]])
            break
        if msg[w:c+1] not in dic:
            dic[msg[w:c+1]] = len(dic) + 1
            answer.append(dic[msg[w:c]])
            w = c

    return answer