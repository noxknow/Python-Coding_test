count = int(input())

cnt = 0
for _ in range(count):
    word = input()
    error = 0
    for index in range(len(word)-1):
        if word[index] != word[index+1]:
            new_word = word[index+1 : ]
            if new_word.count(word[index]) >0 :
                error += 1
    
    if error == 0:
        cnt += 1

print(cnt)
        