import math
def calculate_pythagorean_theorem(a, b):
        return math.sqrt(a**2 + b**2)
def calculate_payback_period(cash_flows):
        cumulative_cash_flow = 0
        for i, cf in enumerate(cash_flows):
        cumulative_cash_flow += cf
        if cumulative_cash_flow >= 0:
                return i
        return None