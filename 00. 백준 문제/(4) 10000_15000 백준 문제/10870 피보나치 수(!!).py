# 재귀함수를 이용한 경우 
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

n = int(input())
print(fibonacci(n))

# for문을 이용한 경우
n = int(input())

fibonacci = [0, 1]
for i in range(2, n+1):
    num = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(num)
print(fibonacci[n])