from itertools import permutations
 
def check(unit, ban):
    for i in range(len(unit)):
        if len(unit[i]) != len(ban[i]): #가져온 tuple과 banned_id의 길이가 맞지않는다면 종료, 이번문제에서 len(unit) = 4 print(unit) 해보면 알 수 있다.
            return False
        for j in range(len(unit[i])): #tuple의 스펠과 baaned_id가 맞지않는다면 종료, "*"는 그대로 진행
            if unit[i][j] != ban[i][j] and ban[i][j] != "*": 
                return False
 
    return True
        
def solution(user_id, banned_id):
    answer = []
    lst = list(permutations(user_id, len(banned_id)))
    for unit in lst: #permutations에서 tuple을 한개씩 가져온다
        if check(unit, banned_id):
            if set(unit) not in answer: #겹치는지 판별
                answer.append(set(unit))
    
    return len(answer) #중복값이 제거된 answer의 길이출력

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
print(solution(user_id, banned_id))

"""
combinations를 쓰지 않는 이유는 banned_id의 순서를 신경 쓰지 않고 진행시켜주기 위함이다.
만약 combinations을 쓴다면 ('frodo', 'fradi')와 ('fradi', 'frodo')는 같은 취급을 받아
사라지게 될텐데 그렇게 된다면 banned_id가 "fr*d*", "*rodo"가 오면 ('fradi', 'frodo')만
정답인데 ('frodo', 'fradi')애랑 합쳐져서 사라질 수가 있으니 permutations 그러고
나중에 set(unit)으로 중복 없애 줌

permutations 한 결과. 
[('frodo', 'fradi'), ('frodo', 'crodo'), ('frodo', 'abc123'), ('frodo', 'frodoc'), ('fradi', 'frodo'),
('fradi', 'crodo'), ('fradi', 'abc123'), ('fradi', 'frodoc'), ('crodo', 'frodo'), ('crodo', 'fradi'),
('crodo', 'abc123'), ('crodo', 'frodoc'), ('abc123', 'frodo'), ('abc123', 'fradi'), ('abc123', 'crodo'),
('abc123', 'frodoc'), ('frodoc', 'frodo'), ('frodoc', 'fradi'), ('frodoc', 'crodo'), ('frodoc', 'abc123')]

unit[i][j]의 의미 unit = [('frodo', 'fradi')]인 경우 unit[0] = frodo 이고, unit[0][0] = f,
unit[0][1] = r 이런 의미.

('frodo', 'crodo', 'abc123', 'frodoc')       ----> 그냥 unit 했을 때, 여기서는 순서가 뒤죽박죽이라
('frodo', 'crodo', 'frodoc', 'abc123')             리스트에 append 할 때 개별로 인식된다.
('fradi', 'frodo', 'abc123', 'frodoc')
('fradi', 'frodo', 'frodoc', 'abc123')
('fradi', 'crodo', 'abc123', 'frodoc')
('fradi', 'crodo', 'frodoc', 'abc123')

{'abc123', 'frodo', 'frodoc', 'crodo'}       ----> set(unit) 했을 때 이때는 리스트에 append를 하면
{'abc123', 'frodo', 'frodoc', 'crodo'}             똑같은것으로 정렬되어있어서 사라지지만
{'abc123', 'frodo', 'frodoc', 'fradi'}
{'abc123', 'frodo', 'frodoc', 'fradi'}
{'abc123', 'crodo', 'frodoc', 'fradi'}
{'abc123', 'crodo', 'frodoc', 'fradi'}


"""