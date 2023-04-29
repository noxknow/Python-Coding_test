N = int(input())  #입력받은 값을 int로 바꿈

for _ in range(N):
    cnt, word = input().split()
    for x in word:
        print(x*int(cnt), end = "")
    print()