import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps