def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)