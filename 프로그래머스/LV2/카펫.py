from itertools import permutations

def solution(brown, yellow):
    answer = []
    
    carpet = brown + yellow
    num_list = []
    for i in range(3, int(carpet**0.5)+1):
        if carpet % i == 0:
            num_list.append((i,carpet//i))
    
    for x,y in num_list:
        if (y-2) * (x-2) == yellow:
            answer += y, x
            
    return answer
