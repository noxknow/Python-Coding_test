def solution(dartResult):
    stack = []
    dartResult = dartResult.replace("10" , "A")
    bonus = {"S" : 1, "D" : 2, "T" : 3}
    
    for i in dartResult:
        if i.isdigit() or i == "A":
            stack.append(10 if i == "A" else int(i))
        elif i.isalpha():
            num = stack.pop()
            stack.append(num ** bonus[i]) # 혹은 한번에 stack[-1] **= bonus[i]
        elif i == "#":
            stack[-1] *= -1
        elif i == "*":
            num = stack.pop()
            if len(stack):
                stack[-1] *= 2
            stack.append(num*2)
            
    return sum(stack)

dartResult = "1D#2S*3S"
print(solution(dartResult))

"""
elif i == "*":                  -->       이것도 가능
    if len(stack) > 1:
        stack[-1] *= 2
        stack[-2] *= 2
    else:
        stack[-1] *= 2
"""