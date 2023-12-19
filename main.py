def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height