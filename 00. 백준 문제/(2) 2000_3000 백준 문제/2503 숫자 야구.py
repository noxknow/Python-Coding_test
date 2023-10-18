import sys
sys.stdin=open("input.txt","r")
input = sys.stdin.readline
from itertools import permutations

n = int(input())

data = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
numList = list(permutations(data, 3))

for _ in range(n):
    number, s, b = map(int, input().split(" "))
    number = list(str(number))
    cnt = 0
    for i in range(len(numList)):
        strike = ball = 0
        i -= cnt
        for j in range(len(number)):
            if number[j] == numList[i][j]:
                strike += 1
            elif number[j] in numList[i]:
                ball += 1
        
        if (strike != s) or (ball != b):
            numList.remove(numList[i])
            cnt += 1

print(len(numList))
