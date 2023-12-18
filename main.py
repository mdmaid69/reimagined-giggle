def calculate_perpetuity(payment, rate):
        return payment / rate
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))