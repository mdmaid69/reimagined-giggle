import math
def calculate_radians_to_degrees(radians):
        return math.degrees(radians)
n = 10
print("Prime numbers:", [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])