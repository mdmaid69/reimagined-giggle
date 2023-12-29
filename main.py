import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps