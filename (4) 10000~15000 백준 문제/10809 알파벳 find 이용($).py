# find 함수 이용
word = input()
alphabet = list(range(97,123))  

for x in alphabet :
    print(word.find(chr(x))) 

# 노가다
S = input()
abc ='abcdefghijklmnopqrstuvwxyz'

for i in abc:
    if i in S:
        print(S.index(i), end= ' ')
    else:
        print( -1, end =' ')

# 아스키 코드를 이용했을때
S = input()
arr = []

for i in range(26):
    arr.append(-1)

for i in range(len(S)):
    if arr[ord(S[i]) - 97] == -1:
        arr[ord(S[i]) - 97] = i
for i in arr:
    print(i, end = ' ')