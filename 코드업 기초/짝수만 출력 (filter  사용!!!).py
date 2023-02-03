# 세 정수 a, b, c가 입력되었을 때, 짝수만 출력해보자
a, b, c = map(int, input().split())
print(*(filter(lambda num: num%2 == 0, [a, b, c]))) # or lambda num : not num%2, [a,b,c]

# 세 정수 a, b, c가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자
a, b, c = map(int, input().split())
print( *map(lambda num: 'odd' if num%2 else 'even', [a, b, c]) )