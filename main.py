import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue