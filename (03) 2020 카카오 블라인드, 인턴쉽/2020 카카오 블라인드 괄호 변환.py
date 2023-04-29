def divide(p):
    open_p = 0
    close_p = 0
    
    for i in range(len(p)):
        if p[i] == "(":
            open_p += 1
        else:
            close_p += 1
        if open_p == close_p:
            return p[:i+1], p[i+1:]

def check(u):
    stack = []

    for p in u:
        if p == "(":
            stack.append(p)
        else:
            if not stack:
                return False
            stack.pop()

    return True

def solution(p):
    answer = ""

    # 과정 1
    if not p:
        return ""

    # 과정 2
    u, v = divide(p)

    # 과정 3
    if check(u):
        # 과정 3-1
        return u + solution(v)
    # 과정 4    
    else:
        # 과정 4-1
        answer += '('
        # 과정 4-2
        answer += solution(v)
        # 과정 4-3
        answer += ')'

        # 과정 4-4
        for p in u[1:len(u) - 1]:
            if p == '(':
                answer += ')'
            else:
                answer += '('

        # 과정 4-5
        return answer

p = "()))((()"
print(solution(p))

# 내 방식
def divide(p):
    
    cnt = 0
    for i in range(len(p)):
        if p[i] == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return p[:i+1], p[i+1:]
            
def solution(p):
    answer = ''
    
    if p == "" :
        return ""
    
    u, v = divide(p)
    
    if u[0] == "(":
        return u + solution(v)
    else:
        answer += "("
        answer += solution(v)
        answer += ")"
        
        for i in u[1:len(u)-1]:
            if i == "(":
                answer += ")"
            else:
                answer += "("
        
        return answer
    
"""
다른 괄호 변환 문제 --- 9012
3
((
))
())(()

a = int(input())
for i in range(a):
    b = input()
    s = list(b)
    sum = 0
    for i in s:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')
"""