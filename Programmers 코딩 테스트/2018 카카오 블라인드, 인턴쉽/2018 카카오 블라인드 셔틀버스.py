def solution(n, t, m, timetable):
    answer = 0
    
    bus_time = []
    for i in range(n):
        bus_time.append(540 + t*i)
    
    crew_time = []
    for time in timetable:
        minute = time.split(":")
        ti = int(minute[0]) * 60 + int(minute[1])
        crew_time.append(ti)
        
    crew_time.sort()
    
    index = 0
    for bus in bus_time:
        cnt = 0 # 버스 시간마다 cnt 초기화
        while cnt < m and index < len(crew_time) and crew_time[index] <= bus:
            cnt += 1
            index += 1
        
        if cnt < m:
            answer = bus
        else:
            answer = crew_time[index-1]-1

    return str(answer//60).zfill(2) + ":" + str(answer%60).zfill(2)

n = 1
t = 1
m = 5
timetable = ["08:00", "08:01", "08:02", "08:03"]
print(solution(n,m,t,timetable))