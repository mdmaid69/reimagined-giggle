import math
def calculate_circle_circumference(radius):
        return 2 * math.pi * radius
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))