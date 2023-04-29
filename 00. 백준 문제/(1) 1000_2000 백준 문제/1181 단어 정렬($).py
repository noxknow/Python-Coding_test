import sys
input = sys.stdin.readline

n = int(input())

words = []
for _ in range(n):
    words.append(input().strip()) # words.append(sys.stdin.readline().strip()) 도 가능

words_list = list(set(words))
words_list.sort() # 길이가 같을때 사전 순 정렬
words_list.sort(key=len)

for i in words_list:
    print(i)
"""
input().split()
input().strip() --> 양쪽 공백을 삭제 (lstrip(왼), rstrip(우))
"""

# 이렇게도 가능
import sys
n = int(sys.stdin.readline())

word = []
for i in range(n):
    word.append(sys.stdin.readline().strip())

set_word = list(set(word))

sort_word = []
for i in set_word:
    sort_word.append((len(i), i)) # 길이까지 같이 표현해 주기 위해서

result = sorted(sort_word)

for len_word, word in result:
    print(word)