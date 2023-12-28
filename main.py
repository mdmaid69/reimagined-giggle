import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets