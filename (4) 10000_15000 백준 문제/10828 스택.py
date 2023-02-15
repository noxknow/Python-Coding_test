import sys
input = sys.stdin.readline

n = int(input())

stack = []
for i in range(n):
  temp = input().split()
  if temp[0] == "push":
    stack.append(temp[1])
  if temp[0] == "top": # elif 나 if 나 상관없을듯.
    if stack:
      print(stack[-1])
    else:
      print(-1)
  if temp[0] == "size":
    print(len(stack))
  if temp[0] == "empty":
    if stack:
      print(0)
    else:
      print(1)
  if temp[0] == "pop":
    if stack:
      print(stack.pop())
    else:
      print(-1)

"""
# if 만 연속 사용.
# 이런식으로 사용할 수 있지만, 이렇게 관계가 있는 것들을 분리할때는
# elif 로 묶어주는것이 더 가독성이 좋지 않을까 싶습니다.
num = 10
if num > 10:
    print("숫자가 10보다 크네요")
if num < 10:    # elif 로 하는것이 가독성에 더 좋음
    print("숫자가 10보다 작네요")
if num == 10:   # elif 혹은 else로 하는것이 가독성에 더 좋음, 이번경우 else가 더 좋
    print("숫자가 10이네요.")


# if 만 연속사용.
# 이렇게 각자 if 문이 처리해야할것들이 독립적인 경우에는 따로따로 해주는것이 맞습니다.
a = "사과"
b = "바나나"
c = "치즈"
if a == "사과":
    print("사과 입니다.")
if b == "바나나":
    print("바나나 입니다.")
if c == "치즈":
    print("치즈 입니다.")
"""