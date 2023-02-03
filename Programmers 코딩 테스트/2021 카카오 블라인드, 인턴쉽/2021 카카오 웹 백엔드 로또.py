def solution(lottos, win_nums):
    answer = []
    win_nums.sort()

    cnt = 0
    for i in range(6):
        if lottos[i] in win_nums:
            cnt += 1

    max_cnt = cnt + lottos.count(0)
    min_cnt = cnt
    
    dic = {0:6, 1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
    answer = [dic[max_cnt], dic[min_cnt]]

    return answer

lottos = [44, 1, 0, 0, 31, 25]	
win_nums = [31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums))