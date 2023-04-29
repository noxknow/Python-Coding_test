def solution(n):
    answer = 0
    
    word = ""
    while n:
        word += str(n%3) 
        n //= 3
    
    answer = int(word,3) # 3진법을 10진법으로 바꿀 때
    
    return answer
