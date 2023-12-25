import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3
def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
                return False
        return True