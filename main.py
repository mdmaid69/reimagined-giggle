import math
def calculate_cartesian_to_polar_coordinates(x, y):
        return math.rect(x, y)
def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                return False
        return True