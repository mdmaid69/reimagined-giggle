import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity