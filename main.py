import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))