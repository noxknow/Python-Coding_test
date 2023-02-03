Case = int(input())

for _ in range(Case):
    score = list(map(int, input().split()))
    score_avg = sum(score[1:]) / score[0]
    cnt = 0 # cnt가 두번째 for 안에 있는경우 반복할때마다 계속 0이 되기때문에 의미가 없어진다.
    for score_list in score[1:]:
        if score_list > score_avg:
            cnt += 1
    rate = cnt / score[0] * 100
    print(f"{rate:.3f}%")

