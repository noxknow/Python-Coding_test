t = int(input())

for _ in range(t):
    l_list = []
    r_list = []
    data = input()
    for i in data:
        if i == '-':
            if l_list: 
                l_list.pop()
        elif i == '<': 
            if l_list:
                r_list.append(l_list.pop())
        elif i == '>': 
            if r_list:
                l_list.append(r_list.pop())
        else:
            l_list.append(i)
    l_list.extend(reversed(r_list)) # 오른쪽 스택에 있는 문자들은 뒤집어서 붙여야 한다.
    print(''.join(l_list))
