Test = int(input())
score = list(map(int, input().split()))
print(score)
max_score = max(score)

new_score = []
for rescore in score:
    new_score.append(rescore / max_score * 100)

test_avg = sum(new_score)/Test
print(test_avg)
