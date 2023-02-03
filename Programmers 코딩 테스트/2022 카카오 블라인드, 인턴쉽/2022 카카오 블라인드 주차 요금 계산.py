import math

def solution(fees, records):
    answer = []
    start = {}
    end = {}
    
    for record in records:
        time, car, enter = record.split()
        hour, minute = time.split(":")
        minutes = int(hour) * 60 + int(minute)

        if enter == "IN":
            start[car] = minutes
        elif enter == "OUT":
            if car in end:
                end[car] += minutes - start[car] # 이미 있으면 두번 입차한거니 += 해줘야 총 주차 시간.
            else:
                end[car] = minutes - start[car] # 총 주차 시간
            del(start[car]) # 출차를 했을테니 start에서 빼준다.

    for key, value in start.items():
        if key in end:
            end[key] += 23*60 + 59 - value # 출차 기록이 없다는 것은 위에서 del(start[car])을 안한거라 start.items()값이 남아 있게 된다.
        else:
            end[key] = 23*60 + 59 - value # 위에거는 입차 출차 입차 한 경우 (+=) 여긴 입차만 한 경우 (=)

    for key, value in end.items():
        time = max(0, value - fees[0]) # 기본 시간보다 주차시간이 적을 때 - 안나오게 하기 위해서
        money = fees[1] + math.ceil(time/fees[2]) * fees[3] # 계산법은 문제에
        end[key] = money

    end = sorted(end.items()) # 2019 카카오 블라인드 실패율 참고 (요거는 키를 기준으로 오름차순 정렬해서 key,val 다 나오게, 나오는 형식은 리스트)

    for key,val in end:
        answer.append(val)
        
    return answer

records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
fees = [180, 5000, 10, 600]
print(solution(fees, records))