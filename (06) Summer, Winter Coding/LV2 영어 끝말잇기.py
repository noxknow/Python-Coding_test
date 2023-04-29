# answer = [dic[i],dic[j]] 이 형식 나왔던거 한번 더 보기 변수 작명 예시 number, order
# def solution(n, words):
#     used_word = []
    
#     used_word.append(words[0])
#     last_word = words[0][-1]
#     number, order = 0, 0
#     for i in range(1, len(words)):
#         if words[i] not in used_word and words[i][0] == last_word:
#             used_word.append(words[i])
#             last_word = words[i][-1]
#         else:
#             number = (i%n) +1
#             order = (i//n) + 1
#             break
    
#     return [number, order]

def solution(n, words):
    
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in words[:i] :
            return [(i%n)+1, (i//n)+1]
        
    return [0,0]
