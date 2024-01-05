import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))