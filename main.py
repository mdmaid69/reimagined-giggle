def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets