import math
def calculate_circle_circumference(radius):
        return 2 * math.pi * radius
def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
                return False
        return True