def convert(num, n):
    T = "0123456789ABCDEF"
    q, r = divmod(num, n)
    if q == 0:
        return T[r]
    else:
        return convert(q, n) + T[r] # 몫이 0이 될 때까지 나머지를 구해야하며 이 과정에서 나온 나머지들을 역순으로 결합해야한다.

# def solution(n, q): ---> 원래는 이런식으로 역순으로 하기도 하는데 위에거가 더 좋은듯?
#     rev_base = ''

#     while n > 0:
#         n, mod = divmod(n, q)
#         rev_base += str(mod)

#     return rev_base[::-1] 
#     # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력
    

def solution(n, t, m, p):
    answer = '' 
    tube = ''
    for num in range(m*t):
        answer+=convert(num, n)

    for i in range(p-1, m*t,m): # p-1(인덱스로 조회하기 위해) 부터 m*t까지 m씩 건너뛰면서 튜브의 값을 조회하여 tube에 붙여줌
        tube += answer[i] 

    return tube # print(tube)

n = 16
t = 16
m = 2
p = 1

solution(n,t,m,p)
