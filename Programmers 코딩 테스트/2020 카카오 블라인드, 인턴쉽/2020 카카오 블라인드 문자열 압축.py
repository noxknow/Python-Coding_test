def solution(s):
    answer = []
    
    if len(s) == 1:
        return 1
    
    for i in range(1, (len(s)//2)+1):
        b = ''
        cnt = 1
        tmp = s[:i]
        for j in range(i, len(s), i):
            if tmp == s[j:i+j]:
                cnt += 1
            else:
                if cnt != 1:
                    b += str(cnt) + tmp
                else:
                    b += tmp
                tmp = s[j:i+j]
                cnt = 1
        if cnt != 1:
            b += str(cnt) + tmp 
        else:
            b += tmp # 마지막 cnt = 1로 초기화 되고, tmp에 c가 남아있기 때문에
        
        answer.append(len(b))
                
    return min(answer)

s = "aabbac"
print(solution(s))

"""
for j in range(i, len(s)+i, i): 하게 된다면 맨 아래 저 부분 안해줘도 된다.
끝까지 더 검사하기 때문에 tmp에 남는게 없어진다.

if cnt != 1:
    b += str(cnt) + tmp 
else:
    b += tmp # 마지막 cnt = 1로 초기화 되고, tmp에 c가 남아있기 때문에
"""