import math
def calculate_radians_to_degrees(radians):
        return math.degrees(radians)
def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
                return False
        return True