# https://programmers.co.kr/learn/courses/30/lessons/17678


def solution(run_count, term_minute, capacity, timetable):
    answer = ''
    crew_count = len(timetable)
    print(crew_count)
    return answer


# 이거 말고 분으로 치환하여 구하는 게 더 좋은 방법 같다.
# 제공받은 문자열을 : 기준으로 하여 배열화하고 앞은 0버리고 x60하여 분을 구하고 뒤는 그냥 더해서 총 분으로 구한다
#


testcase1 = (1, 1, 5, ['08:00', '08:01', '08:02', '08:03'])
testcase2 = (2, 10, 2, ['09:10', '09:09', '08:00'])
testcase3 = (2, 1, 2, ['09:00', '09:00', '09:00', '09:00'])
testcase4 = (1, 1, 5, ['00:01', '00:01', '00:01', '00:01', '00:01'])
testcase5 = (1, 1, 1, ['23:59'])
testcase6 = (10, 60, 45, ['23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59'])

print(solution(*testcase1))
print(solution(*testcase2))
print(solution(*testcase3))
print(solution(*testcase4))
print(solution(*testcase5))
print(solution(*testcase6))
