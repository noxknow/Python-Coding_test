import sys
input = sys.stdin.readline

n = list(map(int, input().strip()))

if 0 not in n: # n.count(0) == 0 으로 해도 된다.
    print(-1)
else:
    if sum(n) % 3 != 0:
        print(-1)
    else:
        n.sort(reverse=True)
        print("".join(map(str, n)))

"""
맨 처음 n = list(map(int, input())) 하게 된다면 결과는 [8, 0, 8, 7, 5, 5] 리스트 안을 
int형으로 인식하고,
n = list(map(input())) 하게 된다면 ['8', '8', '7', '5', '5'] 이런식으로 리스트 안을
str형으로 인식한다.
만약 int으로 인식한다면 0 not in n이 가능하지만 str형으로 인식했으면 "0" not in n으로 해야한다.

"".join()은 안에 str형이 와야하기 때문에 n = list(map(int, input())) 했으면 위처럼
"".join(map(str, n)) 이렇게 바꿔줘야 한다.
n = list(map(input())) 였으면 "".join(n)으로도 가능하다.

오류 메시지를 잘 보시면 아시겠지만, sys.stdin.readline으로 받는 입력은 input()의 끝에 개행문자 
\n이 같이 들어옵니다. 단일 정수를 받을때처럼 n = int(input())과 같이 받는경우는 신경을 안써도 
되는데, 그 외의 경우엔 심심찮게 볼수 있어요. input().strip()을 사용하면 끝의 개행문자등을 
잘라주기때문에, 작성하신 코드의 input() 뒤에 strip()만 붙여주시면 무난하게 통과가 가능합니다 :)
"""