def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                return False
        return True
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)