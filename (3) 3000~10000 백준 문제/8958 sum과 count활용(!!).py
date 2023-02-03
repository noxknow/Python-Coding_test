Case = int(input())

for i in range(Case):
    Test = input()
    s = list(Test)
    sum = 0
    count = 1
    for i in s:
        if i == 'O':
            sum += count
            count += 1
        else:
            count = 1
    print(sum)
