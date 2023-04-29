# 내가 푼 거
a, b, c = map(int, input().split())

if a == b == c:
    print(10000+a*1000)
elif a == b or a == c:
    print(1000+a*100)
elif b == c:
    print(1000+b*100)
else:
    print(100 * max(a,b,c)) # min[a,b]가 아니라 min(a,b)

# 다른 사람이 푼 거 (신박하긴 하지만 직관적이지 않은듯?)
a = list(map(int, input().split()))
a.sort() # 리스트 정렬 (512 면 125로)
b = list(set(a)) # 리스트를 집합화 시켜주고 b에 넣어줌 (336 이면 36으로)

print(a)
print(b)
if len(b) == 3:
    print(100*a[-1])
else:
    print( ( 10**(2-len(b)) ) * ( 1000 + 100 * a[1]) )

"""
의미는 b = list(set(a))를 했을 때 만약 [3, 3, 6]이면 [3, 6]이 되니깐 b의 길이를 통해
같은 수가 몇 개인지 알 수 있고 정렬 할 때 -1부분이 제일 큰 수가 되니 위와같이 쓰게 된다.
else 에서 마지막 a[1]은  3 6 6 혹은 3 3 6에서 중간 부분이므로 무조건 같은 수 이다.
"""
