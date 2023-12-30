import math
def calculate_sign(x):
        return math.copysign(1, x)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps