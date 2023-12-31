def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))