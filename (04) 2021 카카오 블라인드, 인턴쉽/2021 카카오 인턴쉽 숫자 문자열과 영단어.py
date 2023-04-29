def solution(s):
    answer = s
    num = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    
    for item in num.items():
        answer = answer.replace(item[0], str(item[1])) # item[0]는 딕셔너리 key값, item[1]은 딕셔너리 value값
        
    return int(answer) # 위에서 for k,y in num.items() 하고 item[0] = k, item[1] = y 해도 됨

s = "one4seveneight"
print(solution(s))

# 노가다
def solution(s):
    answer = s 
    answer = answer.replace('zero', '0')
    answer = answer.replace('one', '1')
    answer = answer.replace('two', '2')
    answer = answer.replace('three', '3')
    answer = answer.replace('four', '4')
    answer = answer.replace('five', '5')
    answer = answer.replace('six', '6')
    answer = answer.replace('seven', '7')
    answer = answer.replace('eight', '8')
    answer = answer.replace('nine', '9')


    return int(answer)
