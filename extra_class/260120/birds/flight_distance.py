import random

DISTANCE_RANGE = {
    '힘차게': (90, 120),
    '빠르게': (50, 80),
    '부드럽게': (40, 60),
    '퍼덕이며': (10, 30),
    '날지못함': (0, 0)
}

def cal_dis(flight_method: str) -> str:
    min_dis, max_dis = DISTANCE_RANGE.get(flight_method, (0, 0))
    return random.randint(min_dis, max_dis)

    