def calculate_payback_period(cash_flows):
        cumulative_cash_flow = 0
        for i, cf in enumerate(cash_flows):
        cumulative_cash_flow += cf
        if cumulative_cash_flow >= 0:
                return i
        return None
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)