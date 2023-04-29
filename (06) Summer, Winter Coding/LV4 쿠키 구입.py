def solution(cookie):
    answer = 0
    
    for i in range(len(cookie)-1):
        left_sum, left = cookie[i], i
        right_sum, right = cookie[i+1], i+1
        
        while True:
            if left_sum == right_sum:
                answer = max(answer, left_sum)
                
            if left > 0 and left_sum <= right_sum:
                left -= 1
                left_sum += cookie[left]
            elif right < len(cookie)-1 and right_sum <= left_sum:
                right += 1
                right_sum += cookie[right]
            else:
                break
            
    return answer
