def solution(numbers, hand):
    answer = ""
    
    pad = {'1':(0,0), '2':(0,1), '3':(0,2),
           '4':(1,0), '5':(1,1), '6':(1,2),
           '7':(2,0), '8':(2,1), '9':(2,2),
           '*':(3,0), '0':(3,1), '#':(3,2)
        }
        
    left = pad["*"]
    right = pad["#"]

    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            answer += "L"
            left = pad[str(num)]
        elif num == 3 or num == 6 or num == 9:
            answer += "R"
            right = pad[str(num)]
        else:
            left_dis = abs(left[0] - pad[str(num)][0]) + abs(left[1] - pad[str(num)][1])
            right_dis = abs(right[0] - pad[str(num)][0]) + abs(right[1] - pad[str(num)][1])
            
            if left_dis > right_dis:
                answer += "R"
                right = pad[str(num)]
            elif left_dis < right_dis:
                answer += "L"
                left = pad[str(num)]
            else:
                if hand == "right":
                    answer += "R"
                    right = pad[str(num)]
                else: 
                    answer += "L"
                    left = pad[str(num)]
    
    return answer 

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers, hand))

"""
* ### 제출한 코드 ###
if num == 1 or num == 4 or num == 7 :
            answer += 'L'          #answer에 'L' 저장
            left = pad[str(num)]   #해당 번호를 눌렀을 때 왼손의 위치 저장

            
### 수정한 코드 ###
if num in [1,4,7] :
            answer += 'L'          #answer에 'L' 저장
            left = pad[str(num)]   #해당 번호를 눌렀을 때 왼손의 위치 저장


pad[str(num)] = pad["2"], pad["*"] 이런 느낌
pad[str(num)][0] = pad["2"] 의 (0, 1)중 0번째 인덱스 0
pad[str(num)][1] = pad["2"] 의 (0, 1)중 1번째 인덱스 1
"""