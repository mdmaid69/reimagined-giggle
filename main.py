import math
def calculate_remainder(x, y):
        return math.remainder(x, y)
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))