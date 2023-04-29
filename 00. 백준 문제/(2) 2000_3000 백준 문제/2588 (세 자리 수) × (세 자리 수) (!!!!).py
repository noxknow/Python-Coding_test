# 내가 푼거
num1 = int(input())
num2 = input()

print(num1*int(num2[2]), num1*int(num2[1]), num1*int(num2[0]), num1*int(num2), sep = "\n")

# 남이 푼거
a = int(input())
b = input()
for i in range(1,len(b)+1):
    print(a*int(b[-i])) 
print(a*int(b))
"""
b = 385인 경우 b[0] = 3이므로 range(len(b))후에 print(a*int(b[i]))를 하면 
원래 얻는값과 순서가 달라지므로 3 8 5 에서 -1이 5 -2가 8인 것을 이용하여 -i로 표현했다.
"""