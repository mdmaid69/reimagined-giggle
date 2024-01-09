def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets