# https://programmers.co.kr/learn/courses/30/lessons/17678


def solution(run_count, term_minute, capacity, timetable):
    answer = ''
    first_bus_arrived_time = 540
    timetable.sort()
    crew_count = len(timetable)
    boarded_crew_count = 0

    crew_arrive_list = list(map(lambda x: time_to_minute(x), timetable))
    bus_arrive_list = [first_bus_arrived_time]
    current_bus_arrived_time = bus_arrive_list[0]

    for i in range(run_count - 1):
        current_bus_arrived_time += term_minute
        bus_arrive_list.append(current_bus_arrived_time)

    print(bus_arrive_list)

    for i in range(run_count):
        current_bus_capacity = capacity
        for j in range(crew_count):
            if crew_arrive_list[j] <= bus_arrive_list[i]:
                current_bus_capacity -= 1
                boarded_crew_count += 1
                if not current_bus_capacity:
                    break
        if i == run_count - 1:
            if not current_bus_capacity:
                answer = minute_to_time(crew_arrive_list[boarded_crew_count - 1] - 1)
            else:
                answer = minute_to_time(bus_arrive_list[i])

    return answer


def time_to_minute(str_time):
    time_split = str_time.split(':')
    hour = int(time_split[0])
    minute = int(time_split[1])
    return (hour * 60) + minute


def minute_to_time(int_minute):
    hour = int_minute // 60
    minute = int_minute % 60
    return str(hour).zfill(2) + ':' + str(minute).zfill(2)


# 버스의 스케쥴이 나와야 뭐가 된다.
# 이거 말고 분으로 치환하여 구하는 게 더 좋은 방법 같다.
# 제공받은 문자열을 : 기준으로 하여 배열화하고 앞은 0버리고 x60하여 분을 구하고 뒤는 그냥 더해서 총 분으로 구한다

# 소팅해서 먼저온 사람들을 capacity만큼 줄여나간다.


print(solution(1, 1, 5, ['08:00', '08:01', '08:02', '08:03']))
print(solution(2, 10, 2, ['09:10', '09:09', '08:00']))
print(solution(2, 1, 2, ['09:00', '09:00', '09:00', '09:00']))
print(solution(1, 1, 5, ['00:01', '00:01', '00:01', '00:01', '00:01']))
print(solution(1, 1, 1, ['23:59']))
print(solution(10, 60, 45, ['23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59',
                            '23:59', '23:59', '23:59', '23:59', '23:59', '23:59']))