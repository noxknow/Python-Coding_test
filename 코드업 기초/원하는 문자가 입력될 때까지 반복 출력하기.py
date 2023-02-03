# 컴퓨터가 푼것
while True:
     x=input()
     print(x)
     if x=='q':
          break

# 내가 푼것
a = ord(input())
b = ord("q")

while a != b:
    print(chr(a))
    a = ord(input())

print(str("q"))

# 우리밋 식
word = input().split()

for w in word:
  print(w)
  if w == 'q': break


