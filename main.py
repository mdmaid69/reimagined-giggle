import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height
def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
                return False
        return True