import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))