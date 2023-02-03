import math

def solution(enroll, referral, seller, amount):
    parentTree = dict(zip(enroll, referral))
    answer = dict(zip(enroll, [0 for i in range(len(enroll))]))

    for i in range(len(seller)):
        earn = amount[i] * 100
        target = seller[i]
        
        while True:
            if earn < 10:
                answer[target] += earn
                break # break는 while문을 나가게 도와주는 거다. (if를 나갈거는 아니니깐)
            else:
                answer[target] += math.ceil(earn*0.9) # 정수 올림
                if parentTree[target] == "-":
                    break # 여기서도 while을 나가줌. (break는 for, while같은 반복문 나가준다.)
                earn = math.floor(earn*0.1) # 정수 내림
                target = parentTree[target]
       
    return list(answer.values())

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]
print(solution(enroll, referral, seller, amount))