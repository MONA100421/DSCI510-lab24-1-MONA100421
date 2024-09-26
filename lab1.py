# Include your imports here

def simple_interest(principal: float, rate: float, years: float) -> float:
    interest = (principal * rate * years) / 100
    return interest

def uppercase_count(s: str) -> int:
    count = 0
    for c in s:
            if c.isupper():
                count += 1
    return count

import math

def distance_between_points(x1: float, y1: float, x2: float, y2: float) -> float:
    dx = x2 - x1
    dy = y2 - y1
    distance = math.sqrt(dx * dx + dy * dy)
    return distance