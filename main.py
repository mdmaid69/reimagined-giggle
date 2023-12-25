import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
def calculate_roi(gain, cost):
        return (gain - cost) / cost