# 월 입력받아 계절 출력(때때로 수들의 특징을 이용하면 매우 간단히 해결할 수도 있다.)
a = int(input())

if a // 3 == 1:
    print("spring")
elif a // 3 == 2:
    print("summer")
elif a // 3 == 3:
    print("fall")
else:
    print("winter")