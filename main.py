import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding