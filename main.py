import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))