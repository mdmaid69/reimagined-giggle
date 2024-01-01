def calculate_payback_period(cash_flows):
        cumulative_cash_flow = 0
        for i, cf in enumerate(cash_flows):
        cumulative_cash_flow += cf
        if cumulative_cash_flow >= 0:
                return i
        return None
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height