def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding