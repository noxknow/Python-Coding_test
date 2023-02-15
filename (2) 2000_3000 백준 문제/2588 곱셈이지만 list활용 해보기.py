# 버젼 1
A = int(input())
B = int(input())

num_list = []
for num in str(B):
    num_list.append(num)

print(A*int(num_list[2]))
print(A*int(num_list[1]))
print(A*int(num_list[0]))
print(A*B)

# 버젼 2
num1 = int(input())
num2 = input()

print(num1*int(num2[2]), num1*int(num2[1]), num1*int(num2[0]), num1*int(num2), sep = "\n")
