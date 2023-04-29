# 새싹 프린팅
print("         ,r'\"7")
print("r`-_   ,'  ,/")
print(" \\. \". L_r'")
print("   `~\/")
print("      |")
print("      |")

# 간결하게 조건문 이용하기
a, b = map(int, input().split())
print(">" if a > b else ("<" if a < b else "=="))

# 윤년
year = int(input())

if year%4 == 0 and year%100 != 0 or year%400 == 0:
    print("1")
else:
    print("0")