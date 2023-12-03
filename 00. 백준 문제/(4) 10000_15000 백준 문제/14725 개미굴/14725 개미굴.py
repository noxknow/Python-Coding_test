import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())

foodList = []
for i in range(n):
    foods = list(input().split())
    foodList.append(foods[1:])

foodList.sort()

for i in range(n):
    if i == 0:
        for j in range(len(foodList[i])):
            print("--" * j + foodList[i][j])
    else:
        idx = 0  
        for j in range(len(foodList[i])):
            if (foodList[i - 1][j] != foodList[i][j]) or len(foodList[i - 1]) <= j:
                break
            else:
                idx += 1
        for j in range(idx, len(foodList[i])):
            print("--" * j + foodList[i][j])
