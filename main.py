import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
                return False
        return True