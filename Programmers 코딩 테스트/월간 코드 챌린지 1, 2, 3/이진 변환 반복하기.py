def solution(s):
    answer = []
    
    cnt, num = 0, 0
    while s != "1":
        cnt += s.count("0")
        s = s.split("0") # s = s.replace("0","") 도 가능
        s = "".join(s)
        s = bin(len(s))[2:]
        num += 1
        
    answer = [num, cnt]    
    
    return answer
