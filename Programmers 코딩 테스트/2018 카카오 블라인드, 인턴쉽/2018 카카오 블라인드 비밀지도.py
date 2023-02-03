def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        tmp = bin(arr1[i] | arr2[i]) # 비트 연산 or : |, and : &, xor : ^
        tmp = tmp[2:].zfill(n) # zfill을 사용해서 앞에 0이 올 수 있도록 한다. (n=5 일떄, 11111은 문제 없으나 글자 수가 n이 안되는 1111은 앞에 0으로 채워줘야 한다. zfill(n)을 하면 n만큼 부족한 부분을 앞에 0으로 채워준다.)
        tmp = tmp.replace("1", "#").replace("0", " ") # 이것도 가능
        answer.append(tmp)
        
    return answer

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
solution(n, arr1, arr2)

# 노가다
def solution(n, arr1, arr2):
    answer = []
    arr1_bin = []
    arr2_bin = []
    for i in range(n):
        arr1_bin.append(bin(arr1[i])[2:])
        arr2_bin.append(bin(arr2[i])[2:])
        arr1_bin[i] = ("0" * (n - len(arr1_bin[i]))) + arr1_bin[i] # 문자열은 이런식으로 채우기
        arr2_bin[i] = ("0" * (n - len(arr2_bin[i]))) + arr2_bin[i]
        
        tmp = ""
        for p in range(n):
            if arr1_bin[i][p] == "1" or arr2_bin[i][p] == "1":
                tmp += "#"
            elif arr1_bin[i][p] == "0" and arr2_bin[i][p] == "0":
                tmp += " "
        answer.append(tmp)
        
    return answer