import math
def calculate_cartesian_to_polar_coordinates(x, y):
        return math.rect(x, y)
def calculate_payback_period(cash_flows):
        cumulative_cash_flow = 0
        for i, cf in enumerate(cash_flows):
        cumulative_cash_flow += cf
        if cumulative_cash_flow >= 0:
                return i
        return None