import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

s = list(input().strip())
t = list(input().strip())

result = 0
while t:
    if t[-1] == "A":
        t.pop()
    elif t[-1] == "B":
        t.pop()
        t.reverse()

    if s == t:
        result = 1
        break

if result:
    print(1)
else:
    print(0)
