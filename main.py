def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)