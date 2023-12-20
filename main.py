import math
def calculate_hyperbolic_arc_cosine(x):
        return math.acosh(x)
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))