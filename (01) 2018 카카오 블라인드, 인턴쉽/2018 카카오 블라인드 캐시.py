def solution(cacheSize, cities):
    answer = 0
    cache = []
    if cacheSize == 0:
        return len(cities) * 5
    
    for city in cities:
        city = city.upper()
        if city not in cache:
            if len(cache) < cacheSize:
                cache.append(city)
                answer += 5
            else:
                cache.pop(0)
                cache.append(city)
                answer += 5
        
        else:
            cache.pop(cache.index(city))
            cache.append(city)
            answer += 1
                
                       
    return answer

# cachesize = 3
# cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
# print(solution(3, cities))

def solution(cacheSize, cities):
    cache = []
    time = 0
    for city in cities:
        city = city.lower()
        if cacheSize:
            if not city in cache:
                if len(cache) == cacheSize:
                    cache.pop(0)
                cache.append(city)
                time += 5
            else:
                cache.pop(cache.index(city))
                cache.append(city)
                time += 1
        else:
            time += 5
    return time

"""
캐시 교체 알고리즘은 LRU(Least Recently Used)를 사용한다.

사용자에게 빠르게 정보를 제공하기 위해 사용하는 캐시에서 새로운 데이터가 발생했을 때, 
가장 오래전에 사용된 데이터를 제거하고 새로운 데이터를 삽입하는 알고리즘입니다.

새로운 데이터가 들어온 경우
캐시에 넣어준다.
캐시가 가득차있다면, 가장 오래된 데이터를 제거하고 넣어준다.
존재하는 데이터가 들어온 경우
해당 데이터를 꺼낸 뒤,
가장 최근 데이터 위치로 보내준다.
파이썬으로 구현하면 다음과 같습니다.

cache_Size = 5
cache = [1, 2, 3, 4, 5]
user_data = [3, 7, 2]

for data in user_data:
	# Miss!
	if data not in cache:
		if len(cache) < cacheSize:
			cache.append(data)
		else:
			cache.pop(0)
			cache.append(data)
	# Hit!
	else:
		cache.pop(cache.index(data))
		cache.append(data)

# 캐시 결과 확인
print(cache) # [4, 5, 3, 7, 2]
결과를 쫓아가보면,

3은 캐시에 존재합니다. 따라서 최근 위치로 옮겨줍니다. --> [1, 2, 4, 5, 3]
7은 새로운 데이터 입니다. 하지만 그대로 넣어주면 cacheSize를 넘어가므로 가장 오래된 데이터 1을 제거하고 넣어줍니다.
--> [2, 4, 5, 3, 7]
2는 캐시에 존재합니다. 따라서 최근 위치로 옮겨줍니다. --> [4, 5, 3, 7, 2]

cache hit일 경우 실행시간은 1이다.
cache miss일 경우 실행시간은 5이다
"""