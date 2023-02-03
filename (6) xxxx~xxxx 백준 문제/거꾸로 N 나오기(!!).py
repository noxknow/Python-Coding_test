# 내가 한 것
N = int(input())

List = list(range(1,N+1))
List.reverse()
print(*List, sep = "\n")

# 다른사람이 한 것1
print(*range(int(input()),0,-1))

# 다른사람이 한 것2
a=int(input())
for i in range(a,0,-1):
        print(i)