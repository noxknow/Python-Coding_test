def solution(files):
    answer = []
    head, num, tail = "", "", "" # head, num, tail = " ", " ", " " 띄어쓰기면 틀리다.
    
    for file in files:
        for i in range(len(file)):
            if file[i].isdigit():
                head = file[:i]
                num = file[i:]
                
                for j in range(len(num)):
                    if not num[j].isdigit():
                        tail = num[j:]
                        num = num[:j]
                        break
                        
                answer.append([head, num, tail])
                head, num, tail = "", "", ""
                break
                
    answer.sort(key = lambda x : (x[0].lower(), int(x[1]))) # num을 int로 바꾸는 이유는 01이 입력되면 문자열로 인식하기 때문에
    
    return [''.join(i) for i in answer] # for i in answer:, "".join(i) 하는 거랑 똑같음

files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(files))