def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))