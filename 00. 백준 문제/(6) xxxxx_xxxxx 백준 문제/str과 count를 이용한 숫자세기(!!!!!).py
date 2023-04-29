A = int(input())
B = int(input())
C = int(input())

number = list(str(A*B*C))
for i in range(10):
    print(number.count(str(i)))

