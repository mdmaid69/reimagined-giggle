import math
def calculate_neper_number_to_power_x(x):
        return math.exp(x)
def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
                return False
        return True