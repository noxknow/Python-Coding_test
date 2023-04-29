import sys
input = sys.stdin.readline

case = int(input())

num_list = [0] * 10000

for _ in range(case):
    num_list[int(input())] += 1

for i in range(10000):
    if num_list[i] != 0:
        for _ in range(num_list[i]): # ***
            print(i)

# 굳이 *** 안하고 그냥 print(i)해도 될거같은데 하는이유
# --> 그냥 print(i) 하는 경우 5 5 7 이 5 7이 되기 때문에 