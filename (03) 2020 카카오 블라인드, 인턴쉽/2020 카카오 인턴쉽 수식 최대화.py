from itertools import permutations

def calculate(exp, op):
    array = []
    num = ''
    for x in exp:
        if x.isdigit(): # x가 숫자인지 아닌지 판단한다.
            num += x 
        else:
            array.append(num)  
            array.append(x)    
            num = ''
    array.append(num) # 만약 100+200의 경우 마지막 num이 200인데 else로 안들어가니깐 그 부분을 추가하기 위해 마지막에 append해주기    
    
    for o in op:
        stack = []  # 현재 연산을 수행하고 난 후의 결과들 기록
        while len(array) != 0:
            tmp = array.pop(0)
            if tmp == o:
                val = eval(str(stack.pop()) + o + str(array.pop(0)))
                stack.append(val)
            else:
                stack.append(tmp)
        array = stack
    return abs(int(array[0]))


def solution(expression):
    op = ['*', '-', '+'] # 어차피 expression에 없는 연산자는 무시되서 계산됨
    op = list(permutations(op, 3)) # 세개의 연산자를 3P2의 형식으로 조합 해준다.
    answer = 0
    for i in op:
        temp = calculate(expression, i)
        answer = max(answer, temp)
    return answer

expression = "100-200*300-500+20"
print(solution(expression))

"""
x가 str형식이라 += 한다고 더하는게 아니고 100 + 200의 경우 x는 1,0,0,2,0,0 이 되는데 
이때 num += x 한다면 num은 1 10 100이 되고 그 다음에 "+" 이니 else로 가서 array에 추가된 다음
num = "" 에 의해 초기화하고 if i.isdigit()을 통해 다시 2 20 200이 된다.

('*', '-', '+') -> permutation 이런식으로 된다.
('*', '+', '-')
('-', '*', '+')
('-', '+', '*')
('+', '*', '-')
('+', '-', '*')

exp가 이거 100-200*300-500+20 일 때 array = ['100', '-', '200', '*', '300' , '-', '500', '+', '20', ' ', '', ' ', '']
stack에 tmp가 o에 있는 연산자 * - + 과 맞는 경우 array에서는 맨 앞에 있는 숫자가 pop되고
stack에서는 마지막에 있는 숫자가 pop되어 ['100', '-', 60000, '-', '500', '+', '20', ' ', '', ' ', ''] 
array = stack을 통해 저런식으로 바뀌고 두번째 연산자인 - 를 찾아 또 다시
[-60400, '+', '20', ' ', '', ' ', ''] 이런식으로 해서 계산해 나간다.
"""