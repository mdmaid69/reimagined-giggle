def calculate_payback_period(cash_flows):
        cumulative_cash_flow = 0
        for i, cf in enumerate(cash_flows):
        cumulative_cash_flow += cf
        if cumulative_cash_flow >= 0:
                return i
        return None
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)