import sys
input = sys.stdin.readline

n = list(map(int, input().split()))

dic = {0 : 1, 1: 1, 2 : 2, 3 : 2, 4 : 2, 5 : 8} # 혹은 dic = {"0" : 1, "1" : 1 ~~} 으로 하면

for i in range(6):
    print(dic[i] - n[i], end = " ") # 요기서 dic[str(i)]


