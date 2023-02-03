def solution(n, k):
    word = ""
    while n:
        word = str(n%k) + word # 이것은 2진수에서만 통한다.
        n //= k

    word = word.split("0")

    cnt = 0
    for w in word:
        if len(w) == 0: # if 두개 순서 바뀌면 안됨 뒤에게 먼저오면 len(w) == 0인 경우에 int가 안먹어서 Err
            continue
        if int(w) < 2:
            continue
        sosu=True
        for i in range(2,int(int(w)**0.5)+1): # 숫자의 제곱근루트 + 1 --> 소수 찾는 방법
            if int(w)%i==0:
                sosu=False
                break
        if sosu:
            cnt+=1
        
    return cnt

n = 437674
k = 3
print(solution(n,k))
