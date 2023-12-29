import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
import math
def calculate_radians_to_degrees(radians):
        return math.degrees(radians)