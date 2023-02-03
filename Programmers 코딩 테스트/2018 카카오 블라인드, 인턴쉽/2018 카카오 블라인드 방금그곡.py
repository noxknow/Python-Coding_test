def change(music):
    if "A#" in music:
        music = music.replace("A#", "a")
    if "F#" in music:
        music = music.replace("F#", "f")
    if "D#" in music:
        music = music.replace("D#", "d")
    if "C#" in music:
        music = music.replace("C#", "c")
    if "G#" in music:
        music = music.replace("G#", "g")
    return music
    
def solution(m, musicinfos):
    answer = []
    index = 0

    for info in musicinfos:
        index += 1
        music = info.split(",")
        start = music[0].split(":")
        end = music[1].split(":")
        time = (int(end[0]) * 60 + int(end[1])) - (int(start[0]) * 60 + int(start[1])) # 시간 계산 중요

        changed = change(music[3])
        a = len(changed) # 그냥 길이 구하면 # 길이 때문에 이상해지니 소문자로 바꾸기
        b = changed * (time//a) + changed[:time%a] # 이런 생각..
        m = change(m)

        if m in b:
            answer.append([time, index, music[2]])

    answer.sort(key = lambda x: (-x[0], x[1]))
    
    if answer:
        return answer[0][2]
    else:
        return "(None)"
        
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
m = "ABCDEFG"
print(solution(m, musicinfos))

"""
for문을 짤 때 나는 너무 복잡하게 하는것 같다. for문을 여러개 넣는게 아니라 위에 처럼 하나의 for문 안에서
해결이 가능하면 그 생각을 해야하는데..

여기서 change 함수에서 if elif elif 가 아니고 if if if 쓰는 이유는 만약 if elif 라면 if가 성립했을 때
if만 계산하고 아래 elif에 있는 부분은 실행하지 않게 되는데 CD#EF#GAB 이런식으로 들어오면 if elif 라면
CdEF#GAB 이거고 if if 면 CdEfGAB로 둘 다 바꿔주게 된다.
"""